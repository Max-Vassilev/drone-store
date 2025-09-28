import React from "react"
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom"
import Home from "./pages/Home"
import About from "./pages/About"
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
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>

      <footer>
        &copy; 2025 Travel Destinations. All rights reserved.
        <div>
          <a href="contacts.html">Contact Us</a>
        </div>
      </footer>
    </Router>
  )
}
