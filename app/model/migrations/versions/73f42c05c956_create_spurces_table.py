"""Create Spurces Table

Revision ID: 73f42c05c956
Revises: 7a6b060b76b1
Create Date: 2020-11-24 14:53:38.631973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73f42c05c956'
down_revision = '7a6b060b76b1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sources',
        sa.Column('idSource', sa.INTEGER, primary_key=True),
        sa.Column('idManufacturer', sa.INTEGER, sa.ForeignKey("manufacturers.idManufacturer"), nullable=False)
    )

def downgrade():
    op.drop_table('sources')
