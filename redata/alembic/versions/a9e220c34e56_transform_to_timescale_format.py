"""Transform to timescale format

Revision ID: a9e220c34e56
Revises: f3050bf1a56a
Create Date: 2021-02-04 14:29:53.635430

"""
from alembic import op
import sqlalchemy as sa
from redata.models.metrics import (
    MetricsDataDelay,
    MetricsSchemaChanges,
    MetricsDataVolume,
    MetricsDataVolumeDiff,
    MetricsDataValues
)

# revision identifiers, used by Alembic.
revision = 'a9e220c34e56'
down_revision = 'f3050bf1a56a'
branch_labels = None
depends_on = None


all_to_migrate = [
    MetricsDataDelay, MetricsSchemaChanges, MetricsDataVolume,
    MetricsDataVolumeDiff, MetricsDataValues
]

def upgrade():

    for table in all_to_migrate:
        table_name = table.__tablename__

        op.drop_constraint(f'{table_name}_pkey', f'{table_name}', type_='primary')
        op.create_primary_key(f"{table_name}_pkey", f"{table_name}", ["id", "created_at"])
        op.execute(f"""
            SELECT create_hypertable('{table_name}', 'created_at', migrate_data => true)
        """)


def downgrade():

    for table in all_to_migrate:
        table_name = table.__tablename__
        op.drop_constraint(f'{table_name}_pkey', f'{table_name}', type_='primary')
        op.create_primary_key(f"{table_name}_pkey", f"{table_name}", ["id",])