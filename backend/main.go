package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Destination struct {
	Name        string `json:"name"`
	Price       string `json:"price"`
	Days        string `json:"days"`
	Description string `json:"description"`
	Image       string `json:"image"`
}

func destinationsHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Content-Type", "application/json")

	destinations := []Destination{
		{
			Name:        "Paris",
			Price:       "€450",
			Days:        "4 days",
			Description: "Visit the iconic Eiffel Tower, stroll along the Seine, and enjoy the art and culture of the City of Lights.",
			Image:       "https://www.royalcaribbean.com/media-assets/pmc/content/dam/shore-x/paris-le-havre-leh/lh17-paris-sightseeing-without-lunch/stock-photo-skyline-of-paris-with-eiffel-tower-at-sunset-in-paris-france-eiffel-tower-is-one-of-the-most-752725282.jpg?w=1920",
		},
		{
			Name:        "Rome",
			Price:       "€350",
			Days:        "3 days",
			Description: "Discover the Colosseum, Vatican City, and ancient Roman history while savoring Italian cuisine.",
			Image:       "https://www.italyperfect.com/cdn-cgi/image/format=auto,width=1256/https://www.italyperfect.com/g/photos/upload/sml_845543004-1590582528-ip-info-rome.jpg",
		},
		{
			Name:        "Berlin",
			Price:       "€400",
			Days:        "4 days",
			Description: "Explore Berlin's rich history, vibrant nightlife, and world-famous landmarks such as the Brandenburg Gate.",
			Image:       "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Museumsinsel_Berlin_Juli_2021_1_%28cropped%29_b.jpg/2880px-Museumsinsel_Berlin_Juli_2021_1_%28cropped%29_b.jpg",
		},
		{
			Name:        "Madrid",
			Price:       "€380",
			Days:        "3 days",
			Description: "Experience Madrid's royal palaces, bustling plazas, and vibrant nightlife while enjoying delicious Spanish cuisine.",
			Image:       "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltdb42d0af0dddb0dd/65006732539fa162b64ae755/0_-_BCC-2023-MADRID-LANDMARKS-0.webp?format=webp&auto=avif&quality=60&crop=16%3A9&width=1440",
		},
		{
			Name:        "Athens",
			Price:       "€220",
			Days:        "3 days",
			Description: "Explore the Acropolis, stroll through Plaka, and immerse yourself in the rich history and vibrant culture of Greece's capital.",
			Image:       "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Monastiraki_Square_and_Acropolis_in_Athens_%2844149181684%29.jpg/960px-Monastiraki_Square_and_Acropolis_in_Athens_%2844149181684%29.jpg",
		},
		{
			Name:        "Lisbon",
			Price:       "€320",
			Days:        "3 days",
			Description: "Explore the historic Alfama district, savor traditional Portuguese cuisine, and enjoy panoramic views from the city's many miradouros.",
			Image:       "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Lisbon_%2836831596786%29_%28cropped%29.jpg/960px-Lisbon_%2836831596786%29_%28cropped%29.jpg",
		},
	}

	json.NewEncoder(w).Encode(destinations)
}

func main() {
	http.HandleFunc("/destinations", destinationsHandler)

	fmt.Println("Server is running on http://localhost:8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Failed to start server:", err)
	}
}
