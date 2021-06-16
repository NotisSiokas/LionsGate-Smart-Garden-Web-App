from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app.auth import auth
from app.auth.forms.login import *
from app.models import Staff


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = Staff.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('public.index'))
        else:
            flash('Invalid email or password.')

    return render_template('form_page.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))