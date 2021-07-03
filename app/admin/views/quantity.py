from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.project import ProjectForm
from app.admin.forms.quantity import QuantityForm
from app.models import Organisation, Project, Quantity
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/quantity', methods=['GET'])
@login_required
def list_quantity():
    quantity = Quantity.query.all()
    return render_template('admin/quantity.html',
                           rowdata=quantity,
                           title='Quantity')


@admin.route('/quantity/add', methods=['GET', 'POST'])
@login_required
def add_quantity():
    form = QuantityForm()
    if form.validate_on_submit():
        quantity = Quantity(
            sensor_id=form.sensor_id.data,
            quantity_type_id=form.quantity_type_id.data,
            precision=form.precision.data,
        )
        try:
            db.session.add(quantity)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_quantity'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Quantity")


@admin.route('/quantity/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_quantity(id):
    quantity = Quantity.query.get_or_404(id)
    db.session.delete(quantity)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_quantity'))



@admin.route('/quantity/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_quantity(id):
    quantity = Quantity.query.get_or_404(id)
    form = QuantityForm(obj=quantity)

    if form.validate_on_submit():
        quantity.sensor_id = form.sensor_id.data
        quantity.quantity_type_id = form.quantity_type_id.data
        quantity.precision = form.precision.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_quantity'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           quantity=quantity,
                           title='Edit Quantity')
