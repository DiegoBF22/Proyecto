import React from "react";
import { Outlet } from "react-router-dom";
import './cabecera.css';
import logo from "../../assets/logoDatabase.png";

function cabecera(){
    return(<>
        
        <header>
            <a href="/" ><img src={logo} alt="logo" height={"100px"} /></a>
            <a href="/banners">banners</a>
            <a href="/categories">categories</a>
            <a href="/characters">characters</a>
            <a href="/news">news</a>
            <a href="/events">events</a>
            <a href="/about">about</a>
        </header>

        {<Outlet />}
    </>);
}

export default cabecera;