from flask import Blueprint, render_template, request, flash, g

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form # Gets data from the form that did the request
    # if request.method == 'POST' ~~~~
    ## XXX = request.form.get('email')
    if(request.method == 'POST'):
        flash("TESTT", 'error')
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return render_template("login.html")
