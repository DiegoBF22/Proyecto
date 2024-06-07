import React from 'react';
import './notFound.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import news1 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_202404.png';

function notFound() {
    return(
        <div className='notFound'>
            <h1>ERROR 404</h1>
            <h1>This page doesn't exist, maybe you got the url wrong</h1>
        </div>
    );
}

export default notFound;