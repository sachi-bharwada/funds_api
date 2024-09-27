from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
database = os.getenv("DB_NAME")

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://f'{username}':f'{password}'@localhost:5432/f'{database}'"

db.init_app(app)