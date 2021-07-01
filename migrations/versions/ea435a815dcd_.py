"""empty message

Revision ID: ea435a815dcd
Revises: a0eedc7804ee
Create Date: 2021-06-30 21:02:17.785135

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ea435a815dcd'
down_revision = 'a0eedc7804ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('node', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.add_column('sensor_type', sa.Column('model', sa.VARCHAR(length=100), nullable=True))
    op.add_column('sensor_type', sa.Column('datasheet', sa.VARCHAR(length=200), nullable=True))
    op.add_column('site', sa.Column('id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'site', ['project_id'])
    op.drop_column('users', 'profile_text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_text', mysql.VARCHAR(length=200), nullable=True))
    op.drop_constraint(None, 'site', type_='unique')
    op.drop_column('site', 'id')
    op.drop_column('sensor_type', 'datasheet')
    op.drop_column('sensor_type', 'model')
    op.alter_column('node', 'sample_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
