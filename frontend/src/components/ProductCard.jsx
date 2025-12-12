import React from "react"

export default function ProductCard({ product }) {
  return (
    <div className="product-card">
      <img src={product.image} alt={product.name} />

      <div className="product-content">
        <h3>{product.name}</h3>

        <p className="product-details">
          {product.price}
        </p>

        <p>{product.description}</p>

        <button className="product-button">
          View Product
        </button>
      </div>
    </div>
  )
}
