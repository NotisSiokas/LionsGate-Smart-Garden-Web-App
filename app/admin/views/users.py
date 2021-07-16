from flask import render_template, url_for, redirect, flash
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required
from app.admin import admin
from app import db
from app.admin.forms.users import *
from app.models import Users


@admin.route('/user', methods=['GET'])
def list_users():
    users = Users.query.all()
    return render_template('admin/users.html',
                           rowdata=users,
                           title='Users')


@admin.route('/user/add', methods=['GET', 'POST'])

def add_users():
    form = UsersForm()
    if form.validate_on_submit():
        users = Users(
            organisation_id=form.organisation.data.id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            telephone=form.telephone.data,
            password=form.password.data,
        )
        try:
            db.session.add(users)
            db.session.commit()
            flash('New user created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_users'))

    return render_template('form_page.html',
                           form=form,
                           title="Add staff")


@admin.route('/user/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_users(id):
    users = Users.query.get_or_404(id)
    db.session.delete(users)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_users'))


@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_users(id):
    users = Users.query.get_or_404(id)
    form = UsersForm(
        organisation=users.organisation_id,
        first_name=users.first_name,
        last_name=users.last_name,
        email=users.email,
        telephone=users.telephone,
        password_hash=users.password_hash
    )

    if form.validate_on_submit():
        users.organisation_id = form.organisation.data.id
        users.first_name = form.first_name.data
        users.last_name = form.last_name.data
        users.email = form.email.data
        users.telephone = form.telephone.data
        users.password = form.password.data.encode('UTF8')
        try:
            db.session.commit()
            return redirect(url_for('admin.list_users'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')

    return render_template('form_page.html',
                           form=form,
                           users=users,
                           title='Edit users')
