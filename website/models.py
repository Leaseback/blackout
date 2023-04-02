from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sat_name = db.Column(db.String(150))
    disable_code = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    company_name = db.Column(db.String(150))
    contracts = db.relationship('Contract')
