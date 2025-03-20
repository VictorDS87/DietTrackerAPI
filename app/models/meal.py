from database import db
# primary_key - Chave única do Modelo (não é permitido mais de um por modelo) 
# nullable - Indica se o parametro aceita um valor vazio False(não)
# unique - Valor único no banco de dados, pode ter varios campos com ele

# db.String(paramentro) - Define a quantidade máxima de caracteres que vai ser permitido

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Data real
    diet = db.Column(db.Boolean, nullable=False, default=True)  # Exemplo de booleano
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Referência ao usuário

    user = db.relationship('User', backref=db.backref('meals', lazy=True))  # Relacionamento com User

    def __repr__(self):
        return f"<Meal {self.name}>"
