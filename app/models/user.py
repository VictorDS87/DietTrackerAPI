from database import db
from flask_login import UserMixin

# primary_key - Chave única do Modelo (não é permitido mais de um por modelo) 
# nullable - Indica se o parametro aceita um valor vazio False(não)
# unique - Valor único no banco de dados, pode ter varios campos com ele

# db.String(paramentro) - Define a quantidade máxima de caracteres que vai ser permitido

class User(db.Model, UserMixin):
  # id (int), username (text), password (text)
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(255), nullable=False)
  role = db.Column(db.String(80), nullable=False, default='user')