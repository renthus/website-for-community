from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'M8jk07jHGd18yDKJioPhsJWlMg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'

database = SQLAlchemy(app)

from community import routes