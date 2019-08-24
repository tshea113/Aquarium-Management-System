# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app():

    # Create app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'LGjBbVL9_5HwafdH-u6_OA'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Flask-Security Config
    app.config['SECURITY_REGISTERABLE'] = True
    app.config['SECURITY_PASSWORD_SALT'] = 'bms7IDKeC5cZrDBnJgieGw'
    app.config['SECURITY_EMAIL_SENDER'] = 'aquariummanagementsystem@gmail.com'

    # Mail Config
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'aquariummanagementsystem@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ekovpqafntidyhtz'

    db.init_app(app)
    mail.init_app(app)

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