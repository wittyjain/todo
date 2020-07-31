from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.health_check import todo_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(todo_app)
db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)
from app.to_do_app.urls import *

