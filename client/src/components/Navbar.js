import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';

function Navigation() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Navbar.Brand as={Link} to="/" style={{ color: '#f76c0b' }}>Fitness Planner</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link as={Link} to="/" style={{ color: '#f76c0b' }}>Home</Nav.Link>
          <Nav.Link as={Link} to="/workouts" style={{ color: '#f76c0b' }}>Workouts</Nav.Link>
          <Nav.Link as={Link} to="/exercises" style={{ color: '#f76c0b' }}>Exercises</Nav.Link>
          <Nav.Link as={Link} to="/logs" style={{ color: '#f76c0b' }}>Logs</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default Navigation;
