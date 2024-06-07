import React from 'react';
import './about.css';
import gokuA from '../../assets/cartasEjemplo/gokuSSJ3AngelUR.png';
import logo from "../../assets/logoDatabase.png";


function about() {
    return(
        <div class="container">
            <div class="section">
                <div class="header-container">
                    <div className="encapsular">
                   <div class="header-item">
                        <h2>ABOUT US!</h2>
                    </div>
                    </div>
                </div>
                <div class="AboutGrid">
                    <img src={logo} alt="logo"/>
                    <h3>Brief description</h3>
                    <p>With this project I want to make a database that's easily accesible, useful and free to use to everyone. Letting you see each individual card, it's details, animations, links, events, banners...<br></br>
                    This is an ongoing project, so new features and changes to the website will be made in the future. I will also be making a changelog so everyone can see what new things are implemented and when.
                    <br></br>
                    If you want to, you can check the repository for free in <a href='https://github.com/DiegoBF22/Proyecto'>this link</a>.
                    </p>
                </div>
            </div>
        </div>
    );
}

export default about;