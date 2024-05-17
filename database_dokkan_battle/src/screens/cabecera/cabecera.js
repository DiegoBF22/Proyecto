import React from "react";
import { Outlet } from "react-router-dom";
import './cabecera.css';
import logo from "../../assets/logoDatabase.png";

function cabecera(){
    return(<>
        <header>
            <a href="" ><img src={logo} alt="logo" height={"100px"} /></a>
            <a href="">banners</a>
            <a href="">categories</a>
            <a href="">characters</a>
            <a href="">news</a>
            <a href="">events</a>
            <a href="">about</a>
        </header>

        {<Outlet />}
    </>);
}

export default cabecera;