import React, { Component } from 'react';
import './categorias.css';
import { variables } from '../../Variable';

export class Categorias extends Component {
    constructor(props) {
        super(props);

        this.state = {
            originalCategories: [],
            categories: [],
            filters: {
                name: ''
            }
        };

        this.handleFilterChange = this.handleFilterChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    refreshList() {
    fetch(variables.API_URL + 'categories')
        .then(response => response.json())
        .then(data => {
            console.log('Datos de categorías recibidos de la API:', data);
            this.setState({ originalCategories: data, categories: data });
        })
        .catch(error => console.error('Error al llamar a la API de categorías:', error));
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
        }), () => {
            this.applyFilters();
        });
    }

    handleSubmit(event) {
        event.preventDefault();
        this.refreshList();
    }

    applyFilters() {
        const { originalCategories, filters } = this.state;
        const { name } = filters;

        let filteredCategories = originalCategories;

        if (name) {
            filteredCategories = originalCategories.filter(category => category.categoryName.toLowerCase().includes(name.toLowerCase()));
        }

        this.setState({ categories: filteredCategories });
    }

    render() {
        const { categories, filters } = this.state;

        return (
            <div className="container">
                <div className="section">
                    <div className="header-container">
                        <form onSubmit={this.handleSubmit}>
                            <div className="encapsular">
                                <div className="header-item">
                                    <h2>CATEGORIES</h2>
                                    <input
                                        type="text"
                                        className="search-bar"
                                        name="name"
                                        value={filters.name}
                                        placeholder="Category name"
                                        onChange={this.handleFilterChange}
                                    />
                                    <input className="enviar" type="submit" value="search" />
                                </div>
                            </div>
                        </form>
                    </div>
                    <div className="grid">
                        {categories.map((category) => (
                            <a key={category.categoryId} href={`/category/${category.categoryId}`}>
                                <img
                                    src={category.categoryIcon}
                                    alt={category.categoryName}
                                    onError={(e) => { e.target.src = 'path/to/placeholder-image.png'; }}
                                />
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        );
    }
}

export default Categorias;
