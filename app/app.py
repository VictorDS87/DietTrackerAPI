from flask import Flask
from dotenv import load_dotenv
import os
from database import db

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)

@app.route("/hello_world", methods=["GET"])
def hello_world():
  return "Hello world"

if __name__ == '__main__':
  app.run(debug=True)