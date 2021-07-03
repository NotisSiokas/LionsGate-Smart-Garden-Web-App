from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.sensor import SensorForm
from app.models import Sensor
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/sensor', methods=['GET'])
@login_required
def list_sensor():
    sensor = Sensor.query.all()
    return render_template('admin/sensor.html',
                           rowdata=sensor,
                           title='Sensor')


@admin.route('/sensor/add', methods=['GET', 'POST'])
@login_required
def add_sensor():
    form = SensorForm()
    if form.validate_on_submit():
        sensor = Sensor(
            node_id=form.site_id.data,
            sensor_type=form.sensor_type_id.data,
            name=form.name.data,
            description=form.description.data,
            sample_period=form.sample_period.data,
            average_period=form.average_period.data,
        )
        try:
            db.session.add(sensor)
            db.session.commit()
            flash('New sensor created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_sensor'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Sensor")


@admin.route('/Sensor/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_sensor(id):
    sensor = Sensor.query.get_or_404(id)
    db.session.delete(sensor)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_sensor'))



@admin.route('/sensor/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_sensor(id):
    sensor = Sensor.query.get_or_404(id)
    form = SensorForm(obj=sensor)

    if form.validate_on_submit():
        sensor.node_id = form.node_id.data
        sensor.sensor_type_id = form.sensor_type_id.data
        sensor.name = form.name.data
        sensor.description = form.description.data
        sensor.sample_period = form.sample_period.data
        sensor.average_period = form.average_period.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_sensor'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           sensor=sensor,
                           title='Edit sensor')
