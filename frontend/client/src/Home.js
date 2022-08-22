import React from 'react';
import logo from './logo.svg';
import './Home.css';
import NavBar from './NavBar';

function Home() {
    return (
      <div className="Home">
        <header className="Home-header">
          <img src={logo} className="Home-logo" alt="logo" />
          <a
            className="Home-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
          <NavBar />
          </a>
        </header>
      </div>
    );
  }
  
  export default Home;