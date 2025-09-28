from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = [
        {"name": "Paris","price": "€450","days": "4 days","description": "Visit the iconic Eiffel Tower, stroll along the Seine, and enjoy the art and culture of the City of Lights.","image": "..."},
        {"name": "Rome","price": "€350","days": "3 days","description": "Discover the Colosseum, Vatican City, and ancient Roman history while savoring Italian cuisine.","image": "..."},
        {"name": "Berlin","price": "€400","days": "4 days","description": "Explore Berlin's rich history, vibrant nightlife, and world-famous landmarks such as the Brandenburg Gate.","image": "..."},
        {"name": "Madrid","price": "€380","days": "3 days","description": "Experience Madrid's royal palaces, bustling plazas, and vibrant nightlife while enjoying delicious Spanish cuisine.","image": "..."},
        {"name": "Athens","price": "€220","days": "3 days","description": "Explore the Acropolis, stroll through Plaka, and immerse yourself in the rich history and vibrant culture of Greece's capital.","image": "..."},
        {"name": "Lisbon","price": "€320","days": "3 days","description": "Explore the historic Alfama district, savor traditional Portuguese cuisine, and enjoy panoramic views from the city's many miradouros.","image": "..."},
    ]
    return jsonify(destinations)

@app.route("/about", methods=["GET"])
def about_page():
    about_info = {
        "title": "About This Project",
        "description": (
            "This is an example website built with a Flask backend and a React (Vite.js) frontend.\n"
            "Currently, it does not use a database, but PostgreSQL will be added in the future.\n"
            "The project is designed as a small DevOps practice to work with AWS services such as S3, EC2, and RDS\n"
            "(for the future database). Later, it may also be containerized and deployed with ECR and ECS Fargate."
        )
    }
    return jsonify(about_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
