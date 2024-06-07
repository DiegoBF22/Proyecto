import React from 'react';
import './eventType.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import banner1 from '../../assets/bannersAssets/gasha_top_banner_10662.png';
import banner2 from '../../assets/bannersAssets/gasha_top_banner_10618.png';
import banner3 from '../../assets/bannersAssets/gasha_top_banner_10634.png';

function eventType() {
    return(
        <div className="container">
            <div className="section">
                
            <div className="header-container">
                    <div className="encapsular">
                        <div className="header-item">
                            <h2>EVENTS</h2>
                        </div>
                    </div>
                </div>
                <div className="gridEventos">

                    <a href='/events/STORY'>
                        <div className="eventoType">
                            <h3>STORY</h3>
                        </div>
                    </a>
                    <a href='/events/QUEST'>
                        <div className="eventoType">
                            <h3>QUEST</h3>
                        </div>
                    </a>
                    <a href='/events/DB_STORIES'>
                        <div className="eventoType">
                            <h3>DB STORIES</h3>
                        </div>
                    </a>
                    <a href='/events/GROWTH'>
                        <div className="eventoType">
                            <h3>GROWTH</h3>
                        </div>
                    </a>
                    <a href='/events/EZA'>
                        <div className="eventoType">
                            <h3>EXTREME Z BATTLE</h3>
                        </div>
                    </a>
                    <a href='/events/LIMITED'>
                        <div className="eventoType">
                            <h3>LIMITED</h3>
                        </div>
                    </a>
                    <a href='/events/CHALLENGE'>
                        <div className="eventoType">
                            <h3>CHALLENGE</h3>
                        </div>
                    </a>
                    <a href='/events/ULT_CLASH'>
                        <div className="eventoType">
                            <h3>ULTIMATE CLASH</h3>
                        </div>
                    </a>
                    <a href='/events/BURST_MODE'>
                        <div className="eventoType">
                            <h3>BURST MODE</h3>
                        </div>
                    </a>
                    <a href='/events/PETTAN_BATTLE'>
                        <div className="eventoType">
                            <h3>PETTAN BATTLE</h3>
                        </div>
                    </a>

                    
                </div>

            </div>
        </div>
    );
}

export default eventType;