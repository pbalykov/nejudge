from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_nejudge.db'
app.secret_key = 'your-secret-key'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
manager = LoginManager(app)

from app import views, models
