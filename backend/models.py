from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    full_description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)
