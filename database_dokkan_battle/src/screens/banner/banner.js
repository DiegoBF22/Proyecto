import React, { useEffect, useState } from 'react';
import './banner.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import banner1 from '../../assets/bannersAssets/gasha_top_banner_10662.png';
import banner2 from '../../assets/bannersAssets/gasha_top_banner_10618.png';
import banner3 from '../../assets/bannersAssets/gasha_top_banner_10634.png';
import { variables } from '../../Variable';
import { useParams } from 'react-router-dom';

function Banner() {
    const { BannerID } = useParams();
    const [banner, setBanner] = useState(null);
    const [characters, setCharacters] = useState([]);
    
    useEffect(() => {
        fetch(`${variables.API_URL}banners/${BannerID}`)
        .then(response => response.json())
        .then(data => {
            console.log('Datos del banner recibidos de la API:', data); 
            setBanner(data);

            const characterIds = data.bannerCharacters;
            if (characterIds) {
                Promise.all(characterIds.map(id => 
                    fetch(`${variables.API_URL}cards/${id}`).then(response => response.json())
                ))
                .then(characterData => setCharacters(characterData))
                .catch(error => console.error('Error al llamar a la API de personajes:', error));
            }
        })
        .catch(error => console.error('Error al llamar a la API del banner:', error));
}, [BannerID]);
    if (!banner) {
        return <div>Loading...</div>;
    }

    return(
        <div className="container">
            <div className="section">
                <div className="header-container">
                    <div className="encapsular">
                        <div className="header-item">
                            <h2>{banner.bannerName}</h2>
                        </div>
                    </div>
                </div>
                <div className="grid">
                    <div className="texts">
                        <p>
                            {banner.bannerDetails}
                        </p>
                        <img src={banner.bannerIcon} alt="Banner 1" />
                    </div>
                    <div className='fcharacters'>
                        <h2>FEATURED CHARACTERS</h2>
                        {characters.map(character => (
                            <a key={character.cardId} href={`/character/${character.cardId}`}>
                            <img src={character.cardIcon} alt={character.cardName} />
                        </a>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Banner;