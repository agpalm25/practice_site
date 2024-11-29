from flask import Flask
from flask_login import LoginManager
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


load_dotenv()
db = SQLAlchemy()


def create_app() :

    app = Flask(__name__)

    # (madi) 'check if testing app, to configure the app for testing'
    if os.environ.get('CONFIG_TYPE') == 'config.TestingConfig':

        app.config['SECRET_KEY'] = 'secret'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    else:

        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'


    from .models import User
    from .views import mb 
    from .auth import ab

    @login_manager.user_loader
    def load_user(id) :

        return User.query.get(int(id))

    app.register_blueprint(mb)
    app.register_blueprint(ab)

    with app.app_context() :

        print('creating database')
        db.create_all()
    
    return app

if __name__ == '__main__' :
    create_app()

    