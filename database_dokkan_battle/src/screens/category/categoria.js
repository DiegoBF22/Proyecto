import React, { useEffect, useState } from 'react';
import './categoria.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import leader from '../../assets/categoryAssets/Leader.png';
import sub from '../../assets/categoryAssets/Sub.png';
import { variables } from '../../Variable';
import { useParams } from 'react-router-dom';

function Categoria() {
    const { CategoryID } = useParams();
    const [category, setCategory] = useState(null);
    const [characters, setCharacters] = useState([]);
    const [leaders, setLeaders] = useState([]);

    useEffect(() => {
        fetch(`${variables.API_URL}categories/${CategoryID}`)
            .then(response => response.json())
            .then(data => {
                console.log('Datos de la categoría recibidos de la API:', data); 
                setCategory(data);

                const categoryName = data.categoryName;

                fetch(`${variables.API_URL}cards/`)
                    .then(response => response.json())
                    .then(cards => {
                        const filteredLeaders = cards.filter(card => 
                            card.leaderOf && JSON.parse(card.leaderOf).includes(categoryName)
                        );
                        const filteredCharacters = cards.filter(card =>
                            data.categoryCharacters.includes(card.cardId.toString())
                        );
                        setLeaders(filteredLeaders);
                        setCharacters(filteredCharacters);
                    })
                    .catch(error => console.error('Error al llamar a la API de cartas:', error));
            })
            .catch(error => console.error('Error al llamar a la API de la categoría:', error));
    }, [CategoryID]);

    if (!category) {
        return <div>Loading...</div>;
    }

    return (
        <div className="container">
            <div className="section">
                <div className="header-container">
                    <div className="encapsular">
                        <div className="header-item">
                            <img src={category.categoryIcon} alt={category.categoryName} />
                        </div>
                    </div>
                </div>
                <div className="header-container">
                    <div className="encapsular2">
                        <div className="header-item2">
                            <img src={leader} alt="Leader" />
                            <img src={sub} alt="Sub" />
                        </div>
                        <div className="header-item3">
                            {leaders.map(character => (
                                <a key={character.cardId} href={`/character/${character.cardId}`}>
                                    <img src={character.cardIcon} alt={character.cardName} />
                                </a>
                            ))}
                        </div>
                    </div>
                </div>
                <div className="charaGrid">
                    {characters.map(character => (
                        <a key={character.cardId} href={`/character/${character.cardId}`}>
                            <img src={character.cardIcon} alt={character.cardName} />
                        </a>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Categoria;
