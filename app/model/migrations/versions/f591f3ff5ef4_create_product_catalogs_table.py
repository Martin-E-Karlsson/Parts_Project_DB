"""Create Product_catalogs Table

Revision ID: f591f3ff5ef4
Revises: 7e8acc2c1309
Create Date: 2020-11-24 14:52:48.129888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f591f3ff5ef4'
down_revision = '7e8acc2c1309'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product_catalogs',
        sa.Column('idProduct', sa.Integer, sa.ForeignKey("products.idProduct"), primary_key=True),
        sa.Column('idRetailer', sa.Integer, sa.ForeignKey("retailers.idRetailer"), primary_key=True)
    )


def downgrade():
    op.drop_table('product_catalogs')
