from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import mysql.connector
from flask_mail import Mail 
from .config import Config
# import flask migrate here

app = Flask(__name__)

app.config.from_object(Config) 

mail = Mail(app) 
from app import views