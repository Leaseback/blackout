from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class CreateAccCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_acc_code = db.Column(db.Integer)

class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disable_code = db.Column(db.Integer)
    description = db.Column(db.String(150))
    contract = db.Column(db.Integer, db.ForeignKey('contract.id'))

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sat_name = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    codes = db.relationship('Code')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    company_name = db.Column(db.String(150))
    contracts = db.relationship('Contract')
