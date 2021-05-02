from flask import  Flask
from .schedule import schedUpdate

app = Flask(__name__)

from app import views
