"""empty message

Revision ID: 8003717f51e5
Revises: ea435a815dcd
Create Date: 2021-07-01 18:29:59.145216

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8003717f51e5'
down_revision = 'ea435a815dcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('data', 'timestamp_from',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('data', 'timestamp_to',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('data', 'mean',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=False)
    op.alter_column('data', 'min',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=False)
    op.alter_column('data', 'max',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=False)
    op.alter_column('data', 'stdev',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=False)
    op.alter_column('data', 'records',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('node', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('organisation', 'url',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('organisation', 'email',
               existing_type=mysql.VARCHAR(length=60),
               nullable=False)
    op.alter_column('project', 'description',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.alter_column('project', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('project', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('quantity', 'precision',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=False)
    op.alter_column('quantity_type', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('quantity_type', 'unit',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    op.alter_column('sensor', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('sensor', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('sensor', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('site', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('site', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('site', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('users', 'organisation_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'telephone',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('users', 'profile_text',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('users', 'failed_login_attempts',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('users', 'create_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('users', 'archive_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('users', 'confirmation_token',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'display_email_flag',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.drop_index('ix_users_email', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.alter_column('users', 'display_email_flag',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('users', 'confirmation_token',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('users', 'archive_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('users', 'create_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('users', 'failed_login_attempts',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('users', 'profile_text',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.alter_column('users', 'telephone',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'organisation_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('site', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('site', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('site', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('sensor', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('sensor', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('sensor', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('quantity_type', 'unit',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.alter_column('quantity_type', 'name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('quantity', 'precision',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=True)
    op.alter_column('project', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('project', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('project', 'description',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('organisation', 'email',
               existing_type=mysql.VARCHAR(length=60),
               nullable=True)
    op.alter_column('organisation', 'url',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('node', 'average_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('data', 'records',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('data', 'stdev',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=True)
    op.alter_column('data', 'max',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=True)
    op.alter_column('data', 'min',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=True)
    op.alter_column('data', 'mean',
               existing_type=mysql.FLOAT(precision=5, scale=2),
               nullable=True)
    op.alter_column('data', 'timestamp_to',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('data', 'timestamp_from',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###