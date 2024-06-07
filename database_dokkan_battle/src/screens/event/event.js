import React, { useEffect, useState } from 'react';
import './event.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import event1 from '../../assets/eventType/mission_banner_event_zbattle_144.png';
import flag1 from '../../assets/japanFlag.png';
import flag2 from '../../assets/globalFlag.png';
import { variables } from '../../Variable';
import { useParams } from 'react-router-dom';

function Event() {
    const { EventId } = useParams();
    const [event, setEvent] = useState(null);
    const [category, setCategory] = useState(null);

    useEffect(() => {
        fetch(`${variables.API_URL}events/${EventId}`)
            .then(response => response.json())
            .then(data => {
                console.log('Datos de los eventos recibidos de la API:', data); 
                setEvent(data);
            })
            .catch(error => console.error('Error al llamar a la API de los eventos:', error));
    }, [EventId]);

    useEffect(() => {
        if (event) {
            fetch(`${variables.API_URL}categories/`)
                .then(response => response.json())
                .then(data => {
                    const matchedCategory = data.find(cat => cat.categoryName === event.eventWeakness);
                    console.log('Datos de las categorías recibidos de la API:', matchedCategory); 
                    setCategory(matchedCategory);
                })
                .catch(error => console.error('Error al llamar a la API de las categorías:', error));
        }
    }, [event]);

    if (!event) {
        return <div>Loading...</div>;
    }

    return (
        <div className="container">
            <div className="section">
                <div className="header-container">
                    <div className="encapsular">
                        <div className="header-item">
                            <h2>{event.eventName}</h2>
                        </div>
                    </div>
                </div>
                <div className="grid">
                    <div className="texts">
                        <img src={event.eventIcon} alt="event" />
                        <p dangerouslySetInnerHTML={{ __html: event.eventDetails }} />
                    </div>
                    <div className='EventDetails'>
                        <h2>WEAKNESS</h2>
                        {category && (
                            <img src={category.categoryIcon} alt={category.categoryName} />
                        )}
                        <table className='tablaDetalles'>
                            <tr>
                                <th colSpan={2}>RELEASE DATE</th>
                            </tr>
                            <tr>
                                <td>
                                    <img src={flag1} alt="japanFlag"/>
                                    <span>{event.eventReleaseJP || 'N/A'}</span>
                                </td>
                                <td>
                                    <img src={flag2} alt="globalFlag"/>
                                    <span>{event.eventReleaseGL || 'N/A'}</span>
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Event;
