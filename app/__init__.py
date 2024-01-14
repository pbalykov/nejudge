from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_nejudge.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import views, models
