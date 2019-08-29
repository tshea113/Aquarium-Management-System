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