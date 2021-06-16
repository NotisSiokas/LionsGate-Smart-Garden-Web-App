from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.models import SubjectGroup
from app.admin.forms.subject_group import *
from sqlalchemy.exc import SQLAlchemyError


@admin.route('/subject_groups', methods=['GET'])
def list_subject_groups():
    subject_groups = SubjectGroup.query.all()
    return render_template('admin/subject_groups.html',
                           rowdata=subject_groups,
                           title='Subject Groups')


@admin.route('/subject_groups/add', methods=['GET', 'POST'])
def add_subject_group():
    form = SubjectGroupForm()
    if form.validate_on_submit():
        subject_group = SubjectGroup(name=form.name.data)
        try:
            db.session.add(subject_group)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_subject_groups'))

    return render_template('form_page.html',
                           form=form,
                           title="Add subject group")


@admin.route('/subject_group/delete/<int:id>', methods=['GET', 'POST'])
def delete_subject_group(id):
    subject_group = SubjectGroup.query.get_or_404(id)
    db.session.delete(subject_group)
    db.session.commit()

    return redirect(url_for('admin.list_subject_groups'))


@admin.route('/subject_group/edit/<int:id>', methods=['GET', 'POST'])
def edit_subject_group(id):
    subject_group = SubjectGroup.query.get_or_404(id)
    form = SubjectGroupForm(obj=subject_group)

    if form.validate_on_submit():
        subject_group.name = form.name.data
        db.session.commit()
        return redirect(url_for('admin.list_subject_groups'))

    return render_template('form_page.html',
                           form=form,
                           subject_group=subject_group,
                           title='Edit subject group')
