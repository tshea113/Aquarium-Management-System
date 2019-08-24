# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Return a personalized home page for a logged in user
    if not current_user.is_authenticated:
        return render_template('index.html')
    else:
        return render_template('login_index.html', name=current_user.email)

@main.route('/profile')
@login_required
def profile():
    return render_template('login_index.html', name=current_user.email)