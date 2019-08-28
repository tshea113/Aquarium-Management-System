# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

import datetime

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
    user = User.query.filter_by(email=email).first()

    # If a user is found, we want to redirect back to signup page so user can try again
    if user:
        return jsonify('Account already exists!'), 400  # DEBUG

    # Create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(
        first_name=first_name, 
        last_name=last_name, 
        email=email, 
        password=generate_password_hash(password, method='sha256')
        )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201
