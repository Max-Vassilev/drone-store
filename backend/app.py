from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/products", methods=["GET"])
def get_drones():
    drones = [
        {
            "name": "DJI Mini 2 SE",
            "price": "€349",
            "description": "Lightweight drone with 2.7K video, 31-minute flight time, easy controls.",
            "image": "https://s13emagst.akamaized.net/products/53306/53305567/images/res_f0df34e50fd345b71c537306d360eec4.jpg"
        },
        {
            "name": "DJI Air 3",
            "price": "€1099",
            "description": "Dual-camera drone with 4K video and omnidirectional obstacle sensing.",
            "image": "https://store.dji.bg/img/p/8/1/0/2/8102-large_default.jpg"
        },
        {
            "name": "DJI Mavic 3 Classic",
            "price": "€1499",
            "description": "Hasselblad camera drone with 5.1K video for professional creators.",
            "image": "https://s13emagst.akamaized.net/products/50112/50111907/images/res_50f3bef294d609d6fc4143d39a6beb58.jpg"
        },
        {
            "name": "Autel EVO Lite+",
            "price": "€1299",
            "description": "6K video drone with adjustable aperture and strong low-light performance.",
            "image": "https://aerocam.bg/image/cache/catalog/AUTEL/Autel-LITE/autel-lite-plus-dron-nalichen-bulgaria-aerocam-900x900.jpg"
        },
        {
            "name": "Parrot Anafi",
            "price": "€599",
            "description": "4K HDR drone with 180-degree tilt gimbal and ultra-portable design.",
            "image": "https://www.parrot.com/assets/s3fs-public/styles/lg/public/2022-03/anafi-usa.jpg"
        },
        {
            "name": "Skydio 2+",
            "price": "€1,099",
            "description": "Autonomous tracking drone with industry-leading obstacle avoidance.",
            "image": "https://mfe-is.com/wp-content/uploads/2024/09/Skydio-2-Hero.png"
        }
    ]
    return jsonify(drones)

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

@app.route("/contacts", methods=["GET"])
def contacts_page():
    contacts_info = {
        "name": "Maxim Vassilev",
        "title": "Full Stack Web Developer & DevOps Engineer",
        "location": "Sofia, Bulgaria",
        "phone": "+359899849866",
        "github": "https://github.com/Max-Vassilev",
        "linkedin": "https://www.linkedin.com/in/maxim-vassilev-8b9a1721a/"
    }
    return jsonify(contacts_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
