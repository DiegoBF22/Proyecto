import React, { Component } from 'react';
import './inicio.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import news1 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_202404.png';
import { variables } from '../../Variable';

export class Inicio extends Component {

    constructor(props) {
        super(props);

        this.state = {
            cards: [],
            news: []
        }
    }

    refreshList() {
        fetch(variables.API_URL + 'cards')
        .then(response => response.json())
        .then(data => {
            console.log('Datos de cartas recibidos de la API:', data); 
            // Con esto ordena las cartas para mostrar solo las más recientes
            const sortedCards = data.sort((a, b) => b.cardId - a.cardId);
            // Con esto recogeremos solo las 9 primeras cartas
            const firstNineCards = sortedCards.slice(0, 9);
            this.setState({ cards:  firstNineCards });
        })
        .catch(error => console.error('Error al llamar a la API de cartas:', error));
    
        fetch(variables.API_URL + 'news')
            .then(response => response.json())
            .then(data => {
                console.log('Datos de noticias recibidos de la API:', data); 
                // Con esto ordena las noticias para mostrar solo las más recientes
                const sortedNews = data.sort((a, b) => b.newsID - a.newsID);
                const firstThreeNews = sortedNews.slice(0, 3);
                this.setState({ news: firstThreeNews }); 
            })
            .catch(error => console.error('Error al llamar a la API de noticias:', error));
    }

    componentDidMount() {
        this.refreshList();
    }

    render() {
        const { cards, news } = this.state;
        return (
            <div className="InicioContainer">
                <div className="section">
                    <div className="titulo">NEW CHARACTERS</div>
                    <div className="InicioGrid">
                    {cards.map((dep, index) => (
                        <a key={dep.cardId} href={`/character/${dep.cardId}`}>
                            <img
                                src={dep.cardIcon}
                                alt={`Character ${index + 1}: ${dep.cardName}`}
                            />
                        </a>
                    ))}
                    </div>
                </div>
                <div className="section">
                    <div className="titulo">RECENT NEWS</div>
                    <div className="news-list">
                    {news.map((dep, index) => (
                        <a key={dep.newsID} href={`/news/${dep.NewsId}`}>
                            <img
                                src={dep.newsImage}
                                alt={`News ${index + 1}: ${dep.NewsName}`}
                            />
                        </a>
                    ))}
                    </div>
                </div>
            </div>
        );
    }
}

export default Inicio;
