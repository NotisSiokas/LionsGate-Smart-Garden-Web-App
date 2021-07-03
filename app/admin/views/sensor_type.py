from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.sensor import SensorForm
from app.admin.forms.sensor_type import SensorTypeForm
from app.models import Sensor, Sensor_Type
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required




@admin.route('/sensor_type', methods=['GET'])
@login_required
def list_sensor_type():
    sensor_type = Sensor_Type.query.all()
    return render_template('admin/sensor_type.html',
                           rowdata=sensor_type,
                           title='Sensor Type')


@admin.route('/sensor_type/add', methods=['GET', 'POST'])
@login_required
def add_sensor_type():
    form = SensorTypeForm()
    if form.validate_on_submit():
        sensor_type = Sensor_Type(
            manufacturer=form.manufacturer.data,
            url=form.url.data,
            model=form.model.data,
            datasheet=form.datasheet.data,
        )
        try:
            db.session.add(sensor_type)
            db.session.commit()
            flash('New sensor type created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_sensor_type'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Sensor Type")


@admin.route('/Sensor_Type/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_sensor_type(id):
    sensor_type = Sensor_Type.query.get_or_404(id)
    db.session.delete(sensor_type)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_sensor_type'))



@admin.route('/sensor_type/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_sensor_type(id):
    sensor_type = Sensor_Type.query.get_or_404(id)
    form = SensorTypeForm(obj=sensor_type)

    if form.validate_on_submit():
        sensor_type.manufacturer = form.manufacturer.data
        sensor_type.url = form.url.data
        sensor_type.model = form.model.data
        sensor_type.datasheet = form.datasheet.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_sensor_type'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           sensor_type=sensor_type,
                           title='Edit sensor type')
