import React, { Component } from 'react';
import './noticias.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import news1 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_202404.png';
import news2 from '../../assets/newsEjemplo/EN_news_banner_event_915_small.png';
import news3 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_202405.png';
import news4 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_2024042.png';
import news5 from '../../assets/newsEjemplo/EN_news_banner_spshop_20240318_s.png';
import news6 from '../../assets/newsEjemplo/EN_news_banner_spshop_20240514_s.png';
import { variables } from '../../Variable';

export class Noticias extends Component {

    constructor(props) {
        super(props);

        this.state = {
            noticias: []
        };
    }

    refreshList() {
        fetch(variables.API_URL + 'news')
            .then(response => response.json())
            .then(data => {
                console.log('Datos de las noticias recibidos de la API:', data); 
                this.setState({ noticias: data });
            })
            .catch(error => console.error('Error al llamar a la API de noticias:', error));
    }

    componentDidMount() {
        this.refreshList();
    }

    render(){
    return(
        <div class="container">
            <div class="section">
                <div class="header-container">
                    <div className="encapsular">
                        <div class="header-item">
                            <h2>NEWS</h2>
                        </div>
                    </div>
                </div>
                <div class="Newsgrid">
                    {this.state.noticias.map(noticia => (
                        <a key={noticia.newsID} href={`/news/${noticia.newsID}`}>
                            <img src={noticia.newsImage} alt={`News ${noticia.newsID}`} />
                        </a>
                    ))}
                </div>

            </div>
        </div>
    ); 
    }
}

export default Noticias;