# Database designing
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

# Models


class Rider(db.Model, SerializerMixin):
    # Our table  to store the data for our riders
    __tablename__ = 'riders'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    license = db.Column(db.Text, nullable=False, unique=True)
    certificate = db.Column(db.Text, nullable=False, unique=True)
    insurance = db.Column(db.Text, nullable=False, unique=True)
    residence = db.Column(db.Text, nullable=False)


class Lawyer(db.Model, SerializerMixin):

    # Our table to store the data for our lawyers
    __tablename__ = 'lawyers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    degree = db.Column(db.Text, nullable=False)
    residence =db.Column(db.Text,nullable=False)
