from flask import render_template, url_for, redirect, flash
from sqlalchemy.exc import SQLAlchemyError
from app.admin import admin
from app import db
from app.admin.forms.staff import *



@admin.route('/staff/add', methods=['GET', 'POST'])
def list_signup():
    form = Staff()
    if form.validate_on_submit():
        staff = Staff(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data,
            subject_group_id=form.subject_group.data.id,
        )
        try:
            db.session.add(staff)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_signup'))

    return render_template('admin/signup.html',
                           form=form,
                           title="Add staff")


