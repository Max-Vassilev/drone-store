from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = [
        {"name": "Paris","price": "€450","days": "4 days","description": "Visit the iconic Eiffel Tower, stroll along the Seine, and enjoy the art and culture of the City of Lights.","image": "https://www.royalcaribbean.com/media-assets/pmc/content/dam/shore-x/paris-le-havre-leh/lh17-paris-sightseeing-without-lunch/stock-photo-skyline-of-paris-with-eiffel-tower-at-sunset-in-paris-france-eiffel-tower-is-one-of-the-most-752725282.jpg?w=1920"},
        {"name": "Rome","price": "€350","days": "3 days","description": "Discover the Colosseum, Vatican City, and ancient Roman history while savoring Italian cuisine.","image": "https://www.italyperfect.com/cdn-cgi/image/format=auto,width=1256/https://www.italyperfect.com/g/photos/upload/sml_845543004-1590582528-ip-info-rome.jpg"},
        {"name": "Berlin","price": "€400","days": "4 days","description": "Explore Berlin's rich history, vibrant nightlife, and world-famous landmarks such as the Brandenburg Gate.","image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Museumsinsel_Berlin_Juli_2021_1_%28cropped%29_b.jpg/2880px-Museumsinsel_Berlin_Juli_2021_1_%28cropped%29_b.jpg"},
        {"name": "Madrid","price": "€380","days": "3 days","description": "Experience Madrid's royal palaces, bustling plazas, and vibrant nightlife while enjoying delicious Spanish cuisine.","image": "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltdb42d0af0dddb0dd/65006732539fa162b64ae755/0_-_BCC-2023-MADRID-LANDMARKS-0.webp?format=webp&auto=avif&quality=60&crop=16%3A9&width=1440"},
        {"name": "Athens","price": "€220","days": "3 days","description": "Explore the Acropolis, stroll through Plaka, and immerse yourself in the rich history and vibrant culture of Greece's capital.","image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Monastiraki_Square_and_Acropolis_in_Athens_%2844149181684%29.jpg/960px-Monastiraki_Square_and_Acropolis_in_Athens_%2844149181684%29.jpg"},
        {"name": "Lisbon","price": "€320","days": "3 days","description": "Explore the historic Alfama district, savor traditional Portuguese cuisine, and enjoy panoramic views from the city's many miradouros.","image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Lisbon_%2836831596786%29_%28cropped%29.jpg/960px-Lisbon_%2836831596786%29_%28cropped%29.jpg"},
    ]
    return jsonify(destinations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
