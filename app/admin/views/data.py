from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.data import DataForm
from app.models import Data
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/data', methods=['GET'])
@login_required
def list_data():
    data = Data.query.all()
    return render_template('admin/data.html',
                           rowdata=data,
                           title='data')


@admin.route('/data/add', methods=['GET', 'POST'])
@login_required
def data():
    form = DataForm()
    if form.validate_on_submit():
        data = Data(
            quantity_id=form.quantity_id.data,
            timestamp_from=form.timestamp_from.data,
            timestamp_to=form.timestamp_to.data,
            mean=form.mean.data,
            min=form.min.data,
            max=form.max.data,
            stdev=form.stdev.data,
            records=form.records.data,
        )
        try:
            db.session.add(data)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_data'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Data")


@admin.route('/data/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_data(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_data'))



@admin.route('/data/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_data(id):
    data = Data.query.get_or_404(id)
    form = DataForm(
        quantity_id=data.quantity_id,
        timestamp_from = data.timestamp_from,
        timestamp_to = data.timestamp_to,
        mean = data.mean,
        min = data.min,
        max = data.max,
        stdev = data.stdev,
        records = data.records,
    )

    if form.validate_on_submit():
        data.quantity_id = form.name.data
        data.timestamp_from = form.description.data
        data.timestamp_to = form.sample_period.data
        data.mean = form.average_period.data
        data.min = form.min.data
        data.max = form.max.data
        data.stdev = form.stdev.data
        data.records = form.records.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_data'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           data=data,
                           title='Edit Data')
