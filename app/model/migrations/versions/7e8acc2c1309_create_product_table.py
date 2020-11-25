"""Create Product Table

Revision ID: 7e8acc2c1309
Revises: b36e46e1f2c3
Create Date: 2020-11-24 14:52:31.194512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e8acc2c1309'
down_revision = 'b36e46e1f2c3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('idProduct', sa.INTEGER, primary_key=True),
        sa.Column('Name', sa.String(45), nullable=False),
        sa.Column('Retailer', sa.String(45), nullable=False),
        sa.Column('Description', sa.String(45), nullable=False),
        sa.Column('PurchaseCost', sa.INTEGER, nullable=False),
        sa.Column('SellPrice', sa.INTEGER, nullable=False),
        sa.Column('idSource', sa.INTEGER, sa.ForeignKey("sources.idSource"), nullable=False),
        sa.Column('idWarehouse', sa.INTEGER, sa.ForeignKey("warehouses.idWarehouse"), nullable=False)
    )


def downgrade():
    op.drop_table('products')
