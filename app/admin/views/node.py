from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.node import NodeForm
from app.models import Node
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/node', methods=['GET'])
@login_required
def list_node():
    node = Node.query.all()
    return render_template('admin/node.html',
                           rowdata=node,
                           title='Node')


@admin.route('/node/add', methods=['GET', 'POST'])
@login_required
def add_node():
    form = NodeForm()
    if form.validate_on_submit():
        node = Node(
            site_id=form.site_id.data,
            name=form.name.data,
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            description=form.description.data,
            sample_period=form.sample_period.data,
            average_period=form.average_period.data,
        )
        try:
            db.session.add(node)
            db.session.commit()
            flash('New node created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_node'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Node")


@admin.route('/Node/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_node(id):
    node = Node.query.get_or_404(id)
    db.session.delete(node)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_node'))



@admin.route('/node/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_node(id):
    node = Node.query.get_or_404(id)
    form = NodeForm(obj=node)

    if form.validate_on_submit():
        node.site_id = form.site_id.data
        node.name = form.name.data
        node.latitude = form.latitude.data
        node.longitude = form.longitude.data
        node.description = form.description.data
        node.sample_period = form.sample_period.data
        node.average_period = form.average_period.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_node'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           node=node,
                           title='Edit Node')
