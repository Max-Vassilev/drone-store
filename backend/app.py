from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Product

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://drones_user:drones_password@localhost:5432/drones_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "name": p.name,
            "type": p.type,
            "price": p.price,
            "description": p.description,
            "image": p.image
        } for p in products
    ])

@app.route("/about", methods=["GET"])
def about_page():
    return jsonify({
        "title": "About This Project",
        "description": "Flask + React + PostgreSQL + Docker"
    })

@app.route("/contacts", methods=["GET"])
def contacts_page():
    return jsonify({
        "name": "Maxim Vassilev",
        "title": "Full Stack Web Developer & DevOps Engineer",
        "location": "Sofia, Bulgaria"
    })

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=True)