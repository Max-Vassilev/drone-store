import React, { useEffect, useState } from "react"
import "./App.css"

export default function App() {
  const [trips, setTrips] = useState([])

  useEffect(() => {
    async function loadTrips() {
      const res = await fetch("http://localhost:8080/destinations")
      const data = await res.json()
      setTrips(data)
    }
    loadTrips()
  }, [])

  return (
    <>
      <header>
        <h1>Explore Destinations</h1>
      </header>

      <div className="container">
        {trips.map(trip => (
          <div key={trip.name} className="trip-card">
            <img src={trip.image} alt={trip.name} />
            <div className="trip-content">
              <h3>{trip.name}</h3>
              <p className="trip-details">{trip.price} | {trip.days} days</p>
              <p>{trip.description}</p>
              <button className="trip-button">View Trip</button>
            </div>
          </div>
        ))}
      </div>

      <footer>
        &copy; 2025 Travel Destinations. All rights reserved.
        <div>
          <a href="contacts.html" style={{ color: "#60a5fa", textDecoration: "none" }}>
            Contact Us
          </a>
        </div>
      </footer>
    </>
  )
}
