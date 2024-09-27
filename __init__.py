from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database = os.getenv('DB_NAME')

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= f'postgresql://{username}:{password}@localhost:5432/{database}'

db.init_app(app)