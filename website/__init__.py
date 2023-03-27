from flask import Flask

def create_app():
    app = Flask(__name__) # Initialize flask
    app.config['SECRET_KEY'] = 'oimdqwoisdaklmdmd'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # Do you need to go to a prefix to access it? /auth/login


    return app