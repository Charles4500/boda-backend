from app import app
from datetime import datetime
from models import db,Rider,Lawyer,Payment

with app.app_context():
    Rider.query.delete()
    Lawyer.query.delete()
    Payment.query.delete()
