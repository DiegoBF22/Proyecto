import React from 'react';
import './inicio.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import news1 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_202404.png';

function inicio() {
    return(
        <div class="container">
            <div class="section">
                <div class="titulo">NEW CHARACTERS</div>
                <div class="grid">
                    <img src={gokuA} alt="Character 1" />
                    <img src={gokuA} alt="Character 2" />
                    <img src={gokuA} alt="Character 3" />
                    <img src={gokuA} alt="Character 4" />
                    <img src={gokuA} alt="Character 5" />
                    <img src={gokuA} alt="Character 6" />
                    <img src={gokuA} alt="Character 7" />
                    <img src={gokuA} alt="Character 8" />
                    <img src={gokuA} alt="Character 9" />
                </div>
            </div>
            <div class="section">
                <div class="titulo">RECENT NEWS</div>
                <div class="news-list">
                    <img src={news1} alt="News 1" />
                    <img src={news1} alt="News 2" />
                    <img src={news1} alt="News 3" />
                </div>
            </div>
        </div>
    );
}

export default inicio;