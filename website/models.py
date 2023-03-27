from . import db
from flask_login import UserMixin

class SatelliteCodes(db.Model):
    codeId = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    satId = db.Column(db.Integer, db.ForeignKey('satellite.id'))

class Satellite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    codes = db.relationship('SatelliteCodes')
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))