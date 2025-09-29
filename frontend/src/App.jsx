import React from "react"
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom"
import Home from "./pages/Home"
import About from "./pages/About"
import Contacts from "./pages/Contacts"
import "./App.css"

export default function App() {
  return (
    <Router>
      <header>
        <nav>
          <NavLink to="/" className="nav-link">
            <i className="fas fa-house"></i> Home
          </NavLink>
          <NavLink to="/about" className="nav-link">
            <i className="fas fa-info-circle"></i> About
          </NavLink>
          <NavLink to="/contacts" className="nav-link">
            <i className="fas fa-address-book"></i> Contacts
          </NavLink>
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contacts" element={<Contacts />} />
      </Routes>

      <footer>
        &copy; 2025 Travel Destinations. All rights reserved.
      </footer>
    </Router>
  )
}
