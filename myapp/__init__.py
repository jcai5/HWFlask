from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
	SECRET_KEY = 'you-will-never-guess',
	# location of sqlite database
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'appdb'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

db = SQLAlchemy(myapp_obj)

from myapp import routes, models
