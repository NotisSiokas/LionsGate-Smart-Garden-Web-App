from flask import flash, redirect, render_template, url_for, current_app, abort, session, request
from flask_login import login_required, login_user, logout_user, current_user
from flask_mail import Message, Mail
from datetime import datetime
# from flask_simple_captcha import CAPTCHA

from . import auth
from .forms import *
from .. import db
from app.models import User, Company
from app.common import get_this_year
import logging

from ..forms.registration import RegistrationForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        company = Company(
            name='New company',
            description='placeholder',
            address='placeholder',
            city='placeholder',
            post_code='placehldr'
        )
        db.session.add(company)
        db.session.commit()

        user = User(email=form.email.data,
                    username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data,
                    token=form.email.data,
                    company_id=company.id)

        db.session.add(user)
        db.session.commit()

        company.created_by = user.id
        db.session.commit()

        body = """
        Thank you for registering on the Edinburgh Napier University student project exchange.

        To confirm your email address and unlock your account, please click the link below.

        https://projex.napier.ac.uk/auth/confirm/"""

        body += User.generate_token(user.email)

        body += """



        """

        msg = Message(subject="Edinburgh Napier project exchange",
                      body=body,
                      sender="no-reply@projex.napier.ac.uk",
                      recipients=[user.email])
        mail = Mail(current_app)
        mail.send(msg)

        flash('Please check your email inbox')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')