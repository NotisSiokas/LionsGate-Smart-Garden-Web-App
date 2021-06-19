from flask import render_template, url_for, redirect, flash
from sqlalchemy.exc import SQLAlchemyError

from app.admin import admin
from app import db
from app.admin.forms.staff import *



@admin.route('/staff', methods=['GET'])

def list_staff():
    staff = Staff.query.all()
    return render_template('admin/staff.html',
                           rowdata=staff,
                           title='Staff')


@admin.route('/staff/add', methods=['GET', 'POST'])

def add_staff():
    form = StaffForm()
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

        return redirect(url_for('admin.list_staff'))

    return render_template('form_page.html',
                           form=form,
                           title="Add staff")


@admin.route('/staff/delete/<int:id>', methods=['GET', 'POST'])

def delete_staff(id):
    staff = Staff.query.get_or_404(id)
    db.session.delete(staff)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_staff'))


@admin.route('/staff/edit/<int:id>', methods=['GET', 'POST'])

def edit_staff(id):
    staff = Staff.query.get_or_404(id)
    form = StaffForm(
        email = staff.email,
        first_name = staff.first_name,
        last_name = staff.last_name,
        subject_group = staff.subject_group
    )

    if form.validate_on_submit():
        staff.email = form.email.data
        staff.first_name = form.first_name.data
        staff.last_name = form.last_name.data
        staff.password = form.password.data.encode('UTF8')
        staff.subject_group_id = form.subject_group.data.id
        try:
            db.session.commit()
            return redirect(url_for('admin.list_staff'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')

    return render_template('form_page.html',
                           form=form,
                           title='Edit staff')