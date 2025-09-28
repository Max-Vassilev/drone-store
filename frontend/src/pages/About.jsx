import React, { useEffect, useState } from "react"
import "../App.css"

export default function About() {
  const [about, setAbout] = useState(null)

  useEffect(() => {
    async function loadAbout() {
      const res = await fetch("http://54.89.185.135:8080/about") // Hardcoded EC2 IP Address
      const data = await res.json()
      setAbout(data)
    }
    loadAbout()
  }, [])

  if (!about) return <p className="loading-text">Loading...</p>

  return (
    <div className="about-container">
      <h2>{about.title}</h2>
      <p>{about.description}</p>
    </div>
  )
}
