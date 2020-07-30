from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.health_check import todo_app
app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(todo_app)
db = SQLAlchemy(app)

from app.to_do_app.urls import *

db.create_all()

