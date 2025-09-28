import React from "react"

export default function TripCard({ trip }) {
  return (
    <div className="trip-card">
      <img src={trip.image} alt={trip.name} />
      <div className="trip-content">
        <h3>{trip.name}</h3>
        <p className="trip-details">{trip.price} | {trip.days} days</p>
        <p>{trip.description}</p>
        <button className="trip-button">View Trip</button>
      </div>
    </div>
  )
}
