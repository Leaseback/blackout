from flask import Flask

def create_app():
    app = Flask(__name__) # Initialize flask
    app.config['SECRET_KEY'] = 'oimdqwoisdaklmdmd'

    return app