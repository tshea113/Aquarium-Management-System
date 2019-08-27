# main.py

from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from . import db
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)