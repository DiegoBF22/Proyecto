import React, { Component } from 'react';
import './banners.css';
import { variables } from '../../Variable';

export class Banners extends Component {
    constructor(props) {
        super(props);

        this.state = {
            banners: []
        };
    }

    refreshList() {
        fetch(variables.API_URL + 'banners')
            .then(response => response.json())
            .then(data => {
                console.log('Datos de los banners recibidos de la API:', data); 
                this.setState({ banners: data });
            })
            .catch(error => console.error('Error al llamar a la API de banners:', error));
    }

    componentDidMount() {
        this.refreshList();
    }

    render() {
        return (
            <div className="container">
                <div className="section">
                    <div className="header-container">
                        <div className="encapsular">
                            <div className="header-item">
                                <h2>BANNERS</h2>
                            </div>
                        </div>
                    </div>
                    <div className="gridBanners">
                        {this.state.banners.map(banner => (
                            <div className="banner" key={banner.bannerID}>
                                <a key={banner.bannerID} href={`/banners/${banner.bannerID}`}>
                                    <img src={banner.bannerIcon} alt={`Banner ${banner.bannerID}`} />
                                    <h3>{banner.bannerName}</h3>
                                </a>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        );
    }
}

export default Banners;
