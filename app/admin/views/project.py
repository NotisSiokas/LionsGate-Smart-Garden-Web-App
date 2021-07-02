from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.project import ProjectForm
from app.models import Organisation, Project
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/project', methods=['GET'])
@login_required
def list_project():
    project = Project.query.all()
    return render_template('admin/project.html',
                           rowdata=project,
                           title='Project')


@admin.route('/project/add', methods=['GET', 'POST'])
@login_required
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            sample_period=form.sample_period.data,
            average_period=form.average_period.data,
        )
        try:
            db.session.add(project)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_project'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Project")


@admin.route('/project/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_project'))



@admin.route('/project/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.sample_period = form.sample_period.data
        project.average_period = form.average_period.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_project'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           project=project,
                           title='Edit Project')
