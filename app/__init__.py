import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import urlparse

# Initialize Flask app
app = Flask(__name__)

app.config.from_object('config')

# Variable represents sqlalchemy
db = SQLAlchemy(app)

from app import views, model