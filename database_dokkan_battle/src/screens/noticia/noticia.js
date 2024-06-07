import React, { useEffect, useState } from 'react';
import './noticia.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import news from '../../assets/newsEjemplo/EN_news_banner_plain_camp_2024042.png';
import news2 from '../../assets/newAssets/EN_news_banner_plain_camp_2024042.png';
import { variables } from '../../Variable';
import { useParams } from 'react-router-dom';

function Noticia() {

    const { NewsId } = useParams();
    const [news, setNews] = useState(null);
    
    useEffect(() => {
        fetch(`${variables.API_URL}news/${NewsId}`)
        .then(response => response.json())
        .then(data => {
            console.log('Datos de la noticia recibidos de la API:', data); 
            setNews(data);
        })
        .catch(error => console.error('Error al llamar a la API de las news:', error));
    }, [NewsId]);

    if (!news) {
        return <div>Loading...</div>;
    }

    return(
        <div className="container">
            <div className="section">
                <div className="header-container">
                    <div className="encapsular">
                        <div class="header-item">
                            <h2>{news.newsName}</h2>
                        </div>
                    </div>
                </div>
                <div className="Newgrid">
                    <img src={news.newsImage} alt="News Image 1" />
                    <p dangerouslySetInnerHTML={{ __html: news.newsBody }} />
                    <img src={news.newsImage2} alt="News Image 2" />
                </div>

            </div>
        </div>
    );
}

export default Noticia;