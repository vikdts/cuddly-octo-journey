import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import logo from "../assets/logo.png";
import styles from "../styles/NavBar.module.css"
import { NavLink} from 'react-router-dom';

const NavBar = () => {
  return (
    <Navbar className={styles.NavBar} expand="md" fixed="top">
      <Container>
        <NavLink>
        <Navbar.Brand><img src={logo} alt="logo" height="45"/></Navbar.Brand>
        </NavLink>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto text-left">
            <Nav.Link><i className="far fa-circle"></i>Home</Nav.Link>
            <Nav.Link><i className="far fa-arrow-alt-circle-right"></i>Sign in</Nav.Link>
            <Nav.Link><i className="fas fa-user-circle"></i>Sign up</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
