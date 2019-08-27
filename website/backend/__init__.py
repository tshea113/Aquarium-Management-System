# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_mail import Mail
from flask_cors import CORS
from backend.config import *

db = SQLAlchemy()
mail = Mail()

def create_app():

    # Create app
    app = Flask(__name__)

    app.config.from_object('backend.DevelopmentConfig')

    db.init_app(app)
    mail.init_app(app)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    from .models import User, Role

    # Configure Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app