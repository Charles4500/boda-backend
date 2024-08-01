# Database designing
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import check_password_hash

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
class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text,nullable=False)
    lastname = db.Column(db.Text,nullable=False)
    id_no = db.Column(db.Integer,nullable=False)
    phone_no = db.Column(db.Text,nullable=False)
    email = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    area_of_residence = db.Column(db.String,nullable=False)
    

    #Modeling the relationships
    payments = db.relationship('Payment', back_populates='user' )
    reviews = db.relationship('Review', back_populates='user')
    subscriptions = db.relationship('Subscription', back_populates='user')
    cases = db.relationship('Case', back_populates='user')
    lawyer_details = db.relationship('LawyerDetail', back_populates='user')

class LawyerDetail(db.Model,SerializerMixin):
    __tablename__ = 'lawyer_details'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    lawyer_id = db.Column(db.String)
    years_of_experience = db.Column(db.String)
    specialization = db.Column(db.String)
    rate_per_hour = db.Column(db.Integer)
    qualification_certificate = db.Column(db.LargeBinary)

    reviews = db.relationship('Review', back_populates='lawyer')
    cases = db.relationship('Case', back_populates='lawyer')

class Review(db.Model,SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer_details.id'))
    reviews = db.Column(db.String)

class Subscription(db.Model,SerializerMixin):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Case(db.Model,SerializerMixin):
    __tablename__ = 'cases'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyer_details.id'))
    description = db.Column(db.String)
    court_date = db.Column(db.DateTime)
    status = db.Column(db.String)

    case_histories = db.relationship('CaseHistory', back_populates='case')
    messages = db.relationship('Message', back_populates='case', )

class CaseHistory(db.Model,SerializerMixin):
    __tablename__ = 'case_history'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'))
    details = db.Column(db.String)

class Payment(db.Model,SerializerMixin):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    subscriptions = db.relationship('Subscription', back_populates='payment')

class Message(db.Model,SerializerMixin):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'))
    details = db.Column(db.String)
    date = db.Column(db.TIMESTAMP)
    sender_id = db.Column(db.Text)
    receiver_id = db.Column(db.Text)

class Role(db.Model, SerializerMixin):
    __tablename__= 'roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, nullable=False)
    first_name= db.Column(db.Integer, nullable=False)
    Last_name=db.Column(db.Integer, nullable=False)
    email= db.Column(db.Integer,nullable=False)
    
    
    
    