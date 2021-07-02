from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.models import Organisation
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/organisation', methods=['GET'])
@login_required
def list_organisation():
    organisation = Organisation.query.all()
    return render_template('admin/organisation.html',
                           rowdata=organisation,
                           title='Organisations')


@admin.route('/organisation/add', methods=['GET', 'POST'])
@login_required
def add_organisation():
    form = OrganisationForms()
    if form.validate_on_submit():
        organisation = Organisation(
            name=form.name.data,
            address=form.address.data,
            city=form.city.data,
            post_code=form.city.data,
            country=form.country.data,
            url=form.url.data,
            telephone=form.telephone.data,
            email=form.email.data,
            submit=form.submit.data,
        )
        try:
            db.session.add(organisation)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_organisation'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Organisation")


@admin.route('/organisation/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_organisation(id):
    organisation = Organisation.query.get_or_404(id)
    db.session.delete(organisation)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_organisation'))



@admin.route('/organisation/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_organisation(id):
    organisation = Organisation.query.get_or_404(id)
    form = OrganisationForms(obj=organisation)

    if form.validate_on_submit():
        organisation.name = form.name.data
        db.session.commit()
        return redirect(url_for('admin.list_organisation'))

    return render_template('form_page.html',
                           form=form,
                           organisation=organisation,
                           title='Edit Organisation')
