# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#URI格式：mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/grader'
db = SQLAlchemy(app)

from app.routes import login_routes
