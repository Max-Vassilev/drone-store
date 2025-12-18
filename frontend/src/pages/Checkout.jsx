import React, { useState } from "react"
import { useCart } from "../context/CartContext"

export default function Checkout() {
  const { cart } = useCart()

  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    phone: "",
    courier: "",
    address: ""
  })

  const placeOrder = async () => {
    if (
      !form.first_name ||
      !form.last_name ||
      !form.phone ||
      !form.courier ||
      !form.address ||
      cart.length === 0
    ) {
      alert("Please fill all fields")
      return
    }

    try {
      const payload = {
        ...form,
        items: cart.map(i => ({
          product_id: i.id,
          quantity: i.quantity
        }))
      }

      const res = await fetch("http://127.0.0.1:8080/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      })

      if (!res.ok) throw new Error("Request failed")

      localStorage.removeItem("cart")
      alert("Order placed")
      window.location.href = "/"
    } catch (e) {
      alert("Order failed")
    }
  }

  return (
    <div style={{
      maxWidth: "720px",
      margin: "80px auto",
      background: "#ffffff",
      padding: "48px",
      borderRadius: "18px",
      boxShadow: "0 12px 36px rgba(0,0,0,0.12)"
    }}>
      <h2 style={{ marginBottom: "32px" }}>Checkout</h2>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "24px" }}>
        <input className="checkout-input" placeholder="First name"
          onChange={e => setForm({ ...form, first_name: e.target.value })} />

        <input className="checkout-input" placeholder="Last name"
          onChange={e => setForm({ ...form, last_name: e.target.value })} />

        <input className="checkout-input" placeholder="Phone"
          onChange={e => setForm({ ...form, phone: e.target.value })} />

        <select className="checkout-input"
          value={form.courier}
          onChange={e => setForm({ ...form, courier: e.target.value })}>
          <option value="" disabled>Courier</option>
          <option value="speedy">Speedy</option>
          <option value="econt">Econt</option>
        </select>
      </div>

      <textarea className="checkout-textarea" placeholder="Address / Office"
        onChange={e => setForm({ ...form, address: e.target.value })} />

      <button className="checkout-button" onClick={placeOrder}>
        Place Order
      </button>
    </div>
  )
}
