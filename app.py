from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate


#App initialization
app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Hey from flask</h1>'




