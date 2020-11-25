"""Create Warehouses Table

Revision ID: 664033c0cbd1
Revises: 1943bb299637
Create Date: 2020-11-24 14:54:20.998169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664033c0cbd1'
down_revision = '1943bb299637'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'warehouses',
        sa.Column('idWarehouse', sa.INTEGER, primary_key=True),
        sa.Column('ProductInStorage', sa.INTEGER, nullable=False),
        sa.Column('MinimalAmountInStorage', sa.INTEGER, nullable=False),
        sa.Column('AmountToBeDelivered', sa.INTEGER, nullable=False),
        sa.Column('ProductDeliveryDate', sa.DATE)
    )

def downgrade():
    op.drop_table('warehouses')
