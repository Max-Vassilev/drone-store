import React from "react"
import { useNavigate } from "react-router-dom"

export default function ProductCard({ product }) {
  const navigate = useNavigate()

  return (
    <div className="product-card">
      <img src={product.image} alt={product.name} />

      <div className="product-content">
        <h3>{product.name}</h3>
        <p className="product-details">{product.price}</p>
        <p>{product.description}</p>

        <button
          className="product-button"
          onClick={() => navigate(`/products/${product.id}`)}
        >
          View Product
        </button>
      </div>
    </div>
  )
}
