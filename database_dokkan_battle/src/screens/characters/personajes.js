import React, { Component } from 'react';
import './personajes.css';
import { variables } from '../../Variable';

export class Personajes extends Component {
    constructor(props) {
        super(props);

        this.state = {
            cards: [],
            news: [],
            filters: {
                class: '',
                rarity: '',
                name: '',
                type: '',
                sortBy: ''
            }
        };

        this.handleFilterChange = this.handleFilterChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    refreshList() {
        fetch(variables.API_URL + 'cards')
            .then(response => response.json())
            .then(data => {
                const updatedData = data.map(card => ({
                    ...card,
                    categories: card.categories ? card.categories.replace(/"/g, "").split(', ') : [],
                    links: card.links ? card.links.replace(/"/g, "").split(', ') : []
                }));
                console.log('Datos de cartas recibidos de la API:', updatedData);
                this.setState({ cards: updatedData });
            })
            .catch(error => console.error('Error al llamar a la API de cartas:', error));
    }

    componentDidMount() {
        this.refreshList();
    }

    handleFilterChange(event) {
        const { name, value } = event.target;
        this.setState(prevState => ({
            filters: {
                ...prevState.filters,
                [name]: value
            }
        }));
    }

    handleSubmit(event) {
        event.preventDefault();
        this.refreshList();
    }

    applyFilters(cards) {
        const { class: cardClass, rarity, name, type, sortBy } = this.state.filters;

        let filteredCards = cards;

        if (cardClass) {
            filteredCards = filteredCards.filter(card => card.cardClass.toLowerCase() === cardClass.toLowerCase());
        }

        if (rarity) {
            filteredCards = filteredCards.filter(card => card.cardRarity.toLowerCase() === rarity.toLowerCase());
        }

        if (name) {
            filteredCards = filteredCards.filter(card => card.cardName.toLowerCase().includes(name.toLowerCase()));
        }

        if (type) {
            filteredCards = filteredCards.filter(card => card.cardType.toUpperCase() === type.toUpperCase());
        }

        if (sortBy) {
            switch (sortBy) {
                case 'az':
                    filteredCards = filteredCards.sort((a, b) => a.cardName.localeCompare(b.cardName));
                    break;
                case 'za':
                    filteredCards = filteredCards.sort((a, b) => b.cardName.localeCompare(a.cardName));
                    break;
                case 'cardid':
                    filteredCards = filteredCards.sort((a, b) => a.cardId - b.cardId);
                    break;
                case 'release':
                    filteredCards = filteredCards.sort((a, b) => {
                        if (a.releaseJP && b.releaseJP) {
                            return new Date(a.releaseJP) - new Date(b.releaseJP);
                        }
                        return 0;
                    });
                    break;
                default:
                    break;
            }
        }

        return filteredCards;
    }

    render() {
        const { cards, news, filters } = this.state;
        const filteredCards = this.applyFilters(cards);

        return (
            <div className="container">
                <div className="section">
                    <div className="CardFilters">
                        <form onSubmit={this.handleSubmit}>
                            <div className="encapsularCard">
                                <div className="CardFilterItem">
                                    <h3>CLASS</h3>
                                    <select className="header-item" name="class" value={filters.class} onChange={this.handleFilterChange}>
                                        <option value="">SELECT CLASS</option>
                                        <option value="SUPER">SUPER</option>
                                        <option value="EXTREME">EXTREME</option>
                                    </select>
                                </div>

                                <div className="CardFilterItem">
                                    <h3>RARITY</h3>
                                    <select className="header-item" name="rarity" value={filters.rarity} onChange={this.handleFilterChange}>
                                        <option value="">SELECT RARITY</option>
                                        <option value="LR">LR</option>
                                        <option value="UR">UR</option>
                                        <option value="SSR">SSR</option>
                                        <option value="SR">SR</option>
                                        <option value="R">R</option>
                                        <option value="N">N</option>
                                    </select>
                                </div>

                                <div className="CardFilterItem">
                                    <h3>CHARACTERS</h3>
                                    <input
                                        type="text"
                                        className="search-bar"
                                        name="name"
                                        value={filters.name}
                                        placeholder="Character name"
                                        onChange={this.handleFilterChange}
                                    />
                                </div>

                                <div className="CardFilterItem">
                                    <h3>TYPE</h3>
                                    <select className="header-item" name="type" value={filters.type} onChange={this.handleFilterChange}>
                                        <option value="">SELECT TYPE</option>
                                        <option value="AGL">AGL</option>
                                        <option value="STR">STR</option>
                                        <option value="PHY">PHY</option>
                                        <option value="INT">INT</option>
                                        <option value="TEQ">TEQ</option>
                                    </select>
                                </div>

                                <div className="CardFilterItem">
                                    <h3>SHORT BY</h3>
                                    <select className="header-item" name="sortBy" value={filters.sortBy} onChange={this.handleFilterChange}>
                                        <option value="">SELECT ORDER</option>
                                        <option value="az">A-Z</option>
                                        <option value="za">Z-A</option>
                                        <option value="cardid">CARD ID</option>
                                        <option value="release">RELEASE DATE</option>
                                    </select>
                                </div>
                            </div>
                        </form>
                    </div>

                    <div className="CharacterList">
                        {filteredCards.map((dep, index) => (
                            <a key={dep.cardId} href={`/character/${dep.cardId}`}>
                                <img
                                    src={dep.cardIcon}
                                    alt={`Character ${index + 1}: ${dep.cardName}`}
                                />
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        );
    }
}

export default Personajes;
