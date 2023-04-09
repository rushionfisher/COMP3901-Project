from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import mysql.connector
# import flask migrate here

app = Flask(__name__)


from app import views