"""empty message

Revision ID: dd6bfa541a7d
Revises: cb475d4d984f
Create Date: 2021-07-10 16:13:34.856104

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd6bfa541a7d'
down_revision = 'cb475d4d984f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_text',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('users', 'failed_login_attempts',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('users', 'create_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('users', 'archive_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('users', 'confirmation_token',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('users', 'display_email_flag',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'display_email_flag',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('users', 'confirmation_token',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'archive_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('users', 'create_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('users', 'failed_login_attempts',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('users', 'profile_text',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###
