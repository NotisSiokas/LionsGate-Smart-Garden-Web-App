from flask import render_template, url_for, redirect, flash
from app.admin import admin
from app import db
from app.admin.forms.site import SiteForm
from app.models import Organisation, Site
from app.admin.forms.organisation import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required


@admin.route('/site', methods=['GET'])
@login_required
def list_site():
    site = Site.query.all()
    return render_template('admin/site.html',
                           rowdata=site,
                           title='Site')


@admin.route('/Site/add', methods=['GET', 'POST'])
@login_required
def add_site():
    form = SiteForm()
    if form.validate_on_submit():
        site = Site(
            project_id=form.project_id.data.id,
            name=form.name.data,
            description=form.description.data,
            location_polygon=form.location_polygon.data,
            centroid_latitude=form.centroid_latitude.data,
            centroid_longitude=form.centroid_longitude.data,
            sample_period=form.sample_period.data,
            average_period=form.average_period.data,
        )
        try:
            db.session.add(site)
            db.session.commit()
            flash('New record created', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except:
            db.session.rollback()
            flash('An error occurred - no record created', 'error')

        return redirect(url_for('admin.list_site'))

    return render_template('form_page.html',
                           form=form,
                           title="Add Site")


@admin.route('/site/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_site(id):
    site = Site.query.get_or_404(id)
    db.session.delete(site)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        flash('{}'.format(error), 'error')
    except:
        db.session.rollback()
        flash('An error occurred - delete failed', 'error')

    return redirect(url_for('admin.list_site'))



@admin.route('/site/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_site(id):
    site = Site.query.get_or_404(id)
    form = SiteForm(obj=site)

    if form.validate_on_submit():
        site.project_id = form.project_id.data.id
        site.name = form.name.data
        site.description = form.description.data
        site.location_polygon = form.location_polygon.data
        site.centroid_latitude = form.centroid_latitude.data
        site.centroid_longitude = form.centroid_longitude.data
        site.sample_period = form.sample_period.data
        site.average_period = form.average_period.data
        try:
            db.session.commit()
            return redirect(url_for('admin.list_site'))
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__['orig'])
            flash('{}'.format(error), 'error')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred - update failed', 'error')


    return render_template('form_page.html',
                           form=form,
                           site=site,
                           title='Edit Site')
