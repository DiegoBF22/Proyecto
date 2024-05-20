import React from 'react';
import './personajes.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import news1 from '../../assets/newsEjemplo/EN_news_banner_plain_camp_202404.png';

function personajes() {
    return(
        <div class="container">
            <div class="section">
                
            <div class="header-container">
                <form>
                    <div className="encapsular">
                    <div class="header-item">
                        <h3>CLASS</h3>
                        <select class="header-item" name="class" id="class">
                            <option selected disabled>SELECT CLASS</option>
                            <option value="super">SUPER</option>
                            <option value="EXTREME">EXTREME</option>
                        </select>
                    </div>

                    <div class="header-item">
                        <h3>RARITY</h3>
                        <select class="header-item" name="rarity" id="rarity">
                            <option selected disabled>SELECT RARITY</option>
                            <option value="lr">LR</option>
                            <option value="ur">UR</option>
                            <option value="ssr">SSR</option>
                            <option value="sr">SR</option>
                            <option value="r">R</option>
                            <option value="n">N</option>
                        </select>
                    </div>

                   <div class="header-item">
                        <h2>CHARACTERS</h2>
                        <input type="text" class="search-bar" placeholder="Character name"/>
                        <input className="enviar" type="submit" value="search"/>
                    </div>

                    <div class="header-item">
                        <h3>TYPE</h3>
                        <select class="header-item" name="type" id="type">
                            <option selected disabled>SELECT TYPE</option>
                            <option value="agl">AGL</option>
                            <option value="str">STR</option>
                            <option value="phy">PHY</option>
                            <option value="int">INT</option>
                            <option value="teq">TEQ</option>
                        </select>
                    </div>

                    <div class="header-item">
                        <h3>SHORT BY</h3>
                        <select class="header-item" name="shortby" id="shortby">
                            <option selected disabled>SELECT ORDER</option>
                            <option value="az">A-Z</option>
                            <option value="za">Z-A</option>
                            <option value="cardid">CARD ID</option>
                            <option value="release">RELEASE DATE</option>
                        </select>
                    </div>
                    </div>

                </form>
                    
                    
                    
                    
                </div>
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
        </div>
    );
}

export default personajes;