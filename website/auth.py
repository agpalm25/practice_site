from flask import Blueprint, render_template, redirect, url_for, request
from website import db
from .models import User
from flask_login import login_user, login_required, logout_user

ab = Blueprint('auth', __name__)

@ab.route('/sign_up', methods = ['GET', 'POST'])
def sign_up() :
    
    if request.method == 'POST' :

        print('signing up')

        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username = username).first()

        if not existing_user :

            print('creating a new user')

            user = User(username = username)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

        return redirect(url_for('auth.sign_in'))
    
    return render_template('sign_up.html')
        