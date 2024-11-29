from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from website import db
from .models import User

mb = Blueprint('main', __name__)

@mb.route('/', methods=['GET', 'POST'])
def landing() :
    return render_template('landing.html')

