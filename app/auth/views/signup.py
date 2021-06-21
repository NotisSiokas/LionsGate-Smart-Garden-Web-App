from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.testing import db

from app.admin.forms.signup import SignUpForm
from app.auth import auth
from app.auth.forms.login import *
from app.models import Staff
from app import db
from app.auth.forms.password import PasswordForm




@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():

        user = Staff.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('public.index'))
        else:
            flash('Invalid email or password.')

    return render_template('form_page.html', form=form, title='Sign Up')



