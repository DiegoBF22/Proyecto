import React, { useEffect, useState } from 'react';
import './events.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import { variables } from '../../Variable';
import { useParams } from 'react-router-dom';

function Events() {

    const { EventTypeName } = useParams();
    const [events, setEvents] = useState(null);
    
    useEffect(() => {
        fetch(`${variables.API_URL}events/`)
        .then(response => response.json())
        .then(data => {
            console.log('Datos de los eventos recibidos de la API:', data); 
            setEvents(data);
        })
        .catch(error => console.error('Error al llamar a la API de los eventos:', error));
    }, [EventTypeName]);

    if (!events) {
        return <div>Loading...</div>;
    }

    // Filtrar los eventos por el nombre del tipo de evento
    const filteredEvents = events.filter(event => event.eventType === EventTypeName);

    return (
        <div className="container">
            <div className="section">
                <div className="header-container">
                    <form>
                        <div className="encapsular">
                            <div className="header-item">
                                <h2>EVENTS</h2>
                            </div>
                        </div>
                    </form>
                </div>
                <div className="Eventgrid">
                    {filteredEvents.map(event => (
                        <a key={event.eventId} href={`/event/${event.eventId}`}>
                            <img src={event.eventIcon} alt={`Event ${event.eventId}`} />
                        </a>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Events;
