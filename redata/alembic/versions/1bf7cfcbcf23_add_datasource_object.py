"""Add datasource object

Revision ID: 1bf7cfcbcf23
Revises: 793dc222e3ff
Create Date: 2021-02-23 18:23:20.299392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bf7cfcbcf23'
down_revision = '793dc222e3ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('source_type', sa.String(), nullable=True),
    sa.Column('host', sa.String(), nullable=True),
    sa.Column('database', sa.String(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('schemas', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_foreign_key(None, 'alerts_alert', 'monitored_table', ['table_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'alerts_alert', type_='foreignkey')
    op.drop_table('data_source')
    # ### end Alembic commands ###