from database import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_diets = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return f"<Meal {self.average_diets}>"
