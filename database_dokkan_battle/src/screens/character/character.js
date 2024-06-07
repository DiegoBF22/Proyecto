import React, { useEffect, useState } from 'react';
import './character.css';
import flag1 from '../../assets/japanFlag.png';
import flag2 from '../../assets/globalFlag.png';
import { variables } from '../../Variable';
import { useParams } from 'react-router-dom';

function Character() {
    const { CardId } = useParams();

    const [card, setCard] = useState(null);

    useEffect(() => {
        fetch(`${variables.API_URL}cards/${CardId}`)
            .then(response => response.json())
            .then(data => {
                console.log('Datos de cartas recibidos de la API:', data); 
                setCard(data);
            })
            .catch(error => console.error('Error al llamar a la API de la carta:', error));
    }, [CardId]);

    const getBackgroundColor = (cardType) => {
        switch (cardType) {
            case 'AGL':
                return '#045BE1'; // Color para AGL
            case 'TEQ':
                return '#1E7D2D'; // Color para TEQ
            case 'INT':
                return '#8A33AB'; // Color para INT
            case 'STR':
                return '#CC2229'; // Color para STR
            case 'PHY':
                return '#A55703'; // Color para PHY
            default:
                return '#FFFFFF';
        }
    };

    const tableStyle = card ? { backgroundColor: getBackgroundColor(card.cardType) } : {};

    return (
        <div>
            {card && (
                <table className='characterSheet' style={tableStyle}>
                    <tbody>
                        <tr>
                            <th>
                                <img className='CharaIcon' src={card.cardIcon} alt="character icon" />
                            </th>
                            <th>
                                <h2>{card.cardName}</h2>
                            </th>
                            <th>
                                <h2>TYPE</h2>
                                <img className='CharaType' src={card.cardTypeIcon} alt="Character type" />
                            </th>
                            <th>
                                <h2>COST</h2>
                                <h2>{card.cardCost}</h2>
                            </th>
                            <th>
                                <h2>ID</h2>
                                <h2>{card.cardId}</h2>
                            </th>
                        </tr>
                        <tr>
                            <td rowSpan="3">
                                <img className='CharaArt' src={card.cardArt} alt="Character art" />
                            </td>
                            <td colSpan="4">
                                <h2>LEADER SKILL</h2>
                                <p>{card.leader}</p>
                            </td>
                        </tr>
                        <tr>
                            <td colSpan="4">
                                <h2>SUPER ATTACK | {card.nameSA}</h2>
                                <p>{card.sA}</p>
                            </td>
                        </tr>
                        <tr>
                            <td colSpan="4" rowSpan="2">
                                <h2>PASSIVE SKILL | {card.passiveName}</h2>
                                <p>{card.passive}</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <table className='releaseTable' style={tableStyle}>
                                    <tbody>
                                        <tr>
                                            <th colSpan="2">
                                                <h2>RELEASE DATE</h2>
                                            </th>
                                        </tr>
                                        <tr>
                                            <td>  
                                                <img className='CharaIcon' src={flag1} alt="japan flag" />
                                                <h2>{card.releaseJP}</h2>
                                            </td>
                                            <td className='segundaColumna'>  
                                                <img className='CharaIcon' src={flag2} alt="global flag" />
                                                <h2>{card.releaseGB}</h2>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td rowSpan="3">
                                <h2>CATEGORY</h2>
                                <ul>
                                    {Array.isArray(card.categories) ? card.categories.map(category => (
                                        <li key={category}>{category}</li>
                                    )) : <li>{card.categories}</li>}
                                </ul>
                            </td>
                            <td colSpan="4">
                                <h2>ACTIVE SKILL</h2>
                                <p>{card.active}</p>
                            </td>
                        </tr>
                        <tr>
                            <td colSpan="4">
                                <h2>ACTIVATION CONDITIONS</h2>
                                <p>{card.activeConditions}</p>
                            </td>
                        </tr>
                        <tr>
                            <td colSpan="4">
                                <h2>LINKS</h2>
                                <p>{Array.isArray(card.links) ? card.links.join(', ') : card.links}</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <h2>OBTAINED FROM</h2>
                                <img className='CharaIcon' src={card.obtainedFrom} alt="Character type" />
                            </td>
                            <td colSpan="4">
                                <table className='statsTable' style={tableStyle}>
                                    <tbody>
                                        <tr>
                                            <th><h2>STATS</h2></th>
                                            <th><h2>BASE</h2></th>
                                            <th><h2>MAX LV</h2></th>
                                            <th><h2>55%</h2></th>
                                            <th><h2>100%</h2></th>
                                        </tr>
                                        <tr>
                                            <td>HP</td>
                                            <td>{card.baseHP}</td>
                                            <td>{card.maxHP}</td>
                                            <td>{card.hp55}</td>
                                            <td>{card.hp100}</td>
                                        </tr>
                                        <tr>
                                            <td>ATK</td>
                                            <td>{card.baseATK}</td>
                                            <td>{card.maxATK}</td>
                                            <td>{card.atk55}</td>
                                            <td>{card.atk100}</td>
                                        </tr>
                                        <tr>
                                            <td>DEF</td>
                                            <td>{card.baseDEF}</td>
                                            <td>{card.maxDEF}</td>
                                            <td>{card.def55}</td>
                                            <td>{card.def100}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            )}
        </div>
    );
}

export default Character;
