from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)

''' app.config['SECRET_KEY'] = "Som3$ec5etK*y"  # you should make this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:lab5@localhost/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning '''

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(Config)
from app import views
