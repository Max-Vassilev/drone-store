import React, { useEffect, useState } from "react"
import TripCard from "../components/TripCard"

export default function Home() {
  const [trips, setTrips] = useState([])

  useEffect(() => {
    async function loadTrips() {
      const res = await fetch("http://54.89.185.135:8080/destinations") // Hardcoded EC2 IP Address
      const data = await res.json()
      setTrips(data)
    }
    loadTrips()
  }, [])

  return (
    <div className="container">
      {trips.map(trip => (
        <TripCard key={trip.name} trip={trip} />
      ))}
    </div>
  )
}
