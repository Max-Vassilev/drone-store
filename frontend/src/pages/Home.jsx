import React, { useEffect, useState } from "react"
import TripCard from "../components/TripCard"

export default function Home() {
  const [trips, setTrips] = useState(null)

  useEffect(() => {
    fetch("http://54.89.185.135:8080/destinations") // Hardcoded EC2 IP Address
      .then(res => res.json())
      .then(data => setTrips(data))
  }, [])

  if (!trips) return <div className="loading-text">Loading...</div>

  return (
    <div className="container">
      {trips.map(trip => (
        <TripCard key={trip.name} trip={trip} />
      ))}
    </div>
  )
}
