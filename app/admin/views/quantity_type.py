from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.project import ProjectForm
from app.admin.forms.quantity import QuantityForm
from app.admin.forms.quantity_type import Quantity_Type_Form
from app.models import Organisation, Project, Quantity, Quantity_Type
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/quantity_type', methods=['GET'])
@login_required
def list_quantity_type():
    quantity_type = Quantity_Type.query.all()
    return render_template('admin/quantity_type.html',
                           rowdata=quantity_type,
                           title='Quantity_type')


@admin.route('/quantity_type/add', methods=['GET', 'POST'])
@login_required
def add_quantity_type():
    form = Quantity_Type_Form()
    if form.validate_on_submit():
        quantity_type = Quantity_Type(
            name=form.name.data,
            unit=form.unit.data,
            symbol=form.symbol.data,
        )
        try:
            db.session.add(quantity_type)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_quantity_type'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Quantity_type")


@admin.route('/quantity_type/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_quantity_type(id):
    quantity_type = Quantity_Type.query.get_or_404(id)
    db.session.delete(quantity_type)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_quantity_type'))



@admin.route('/quantity_type/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_quantity_type(id):
    quantity_type = Quantity_Type.query.get_or_404(id)
    form = Quantity_Type_Form(obj=quantity_type)

    if form.validate_on_submit():
        quantity_type.name = form.name.data
        quantity_type.unit= form.unit.data
        quantity_type.symbol = form.symbol.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_quantity_type'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           quantity_type=quantity_type,
                           title='Edit Quantity Type')
