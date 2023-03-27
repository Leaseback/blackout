from flask import Blueprint, render_template, request, flash, g
from .models import User
from sqlalchemy import Engine,text
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form # Gets data from the form that did the request
    # if request.method == 'POST' ~~~~
    #flash("TESTT", 'error')
    ## XXX = request.form.get('email')
    if(request.method == 'POST'):
        username = request.form.get('name')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if not user:
            rs = db.session.execute(text("SELECT * FROM user WHERE username='" + username +"' AND password='+password'"))
            print('executing: ')
            print(rs)
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return render_template("login.html")
