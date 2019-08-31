# auth.py

from flask import Blueprint, redirect, request, jsonify
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from .models import User
from . import db
from backend.config import Config
from functools import wraps

import jwt

auth = Blueprint('auth', __name__)

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return redirect('/')

        try:
            token = auth_headers[1]
            data = jwt.decode(token, Config.SECRET_KEY)
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                return redirect('/')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return redirect('/')
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return redirect('/')

    return _verify

@auth.route('/signup', methods=['POST'])
def register():
    # Get the registration data from the request
    data = request.json
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    # If this returns a user, then the email already exists in database
    user = User.authenticate(**data)

    # If a user is found, we want to redirect back to signup page so user can try again
    if user:
        return jsonify('Account already exists!'), 400  # DEBUG

    # Create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(
        first_name,
        last_name,
        email,
        password
        )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

@auth.route('/login', methods=['POST'])
def login():
    # Get the login data from the request
    data = request.json

    # Find the user
    user = User.authenticate(**data)

    # Catch bad inputs
    if not user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        Config.SECRET_KEY)

    return jsonify({ 'token': token.decode('UTF-8') })

@auth.route('/getDashboard', methods=['GET'])
@token_required
def dashboard(current_user):
    message = "Hello, " + current_user.first_name
    return jsonify({ 'message': message })