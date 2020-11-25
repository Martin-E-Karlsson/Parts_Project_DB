"""Create Manufacturer Table

Revision ID: 35d4ad3f9b29
Revises: 1271021e9d20
Create Date: 2020-11-24 14:51:47.695414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35d4ad3f9b29'
down_revision = '1271021e9d20'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacturers',
        sa.Column('idManufacturer',sa.INTEGER, primary_key=True),
        sa.Column('HQAdress',sa.String(45), nullable=False),
        sa.Column('HQPhoneNumber',sa.String(45), nullable=False),
        sa.Column('ManufacturerName',sa.String(155), nullable=False)
    )


def downgrade():
    op.drop_table('manufacturers')
