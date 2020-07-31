import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = os.environ["DEBUG"]
HOST = os.environ["HOST"]
PORT = os.environ["PORT"]
DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
SQLALCHEMY_DATABASE_URI = f"postgres://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQL_TRACK_MODIFICATIONS = False
API_TOKEN = os.environ["API_TOKEN"]
