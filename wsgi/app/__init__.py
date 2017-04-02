from flask import Flask
import os

app = Flask(__name__)

app.secret_key = os.environ['APIKEY']

from app import views, simple


