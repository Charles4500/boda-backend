#Making the views
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from models import db

# App initialization
app = Flask(__name__)
api = Api(app)


# Config the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boda.db'


CORS(app)
migrate = Migrate(app,db,render_as_batch=True)

db.init_app(app)

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return '<h1>Hey from flask</h1>'
