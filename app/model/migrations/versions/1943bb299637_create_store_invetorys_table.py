"""Create Store_invetorys Table

Revision ID: 1943bb299637
Revises: 86b27247da41
Create Date: 2020-11-24 14:54:10.147056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1943bb299637'
down_revision = '86b27247da41'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'storeinventorys',
        sa.Column('idProduct', sa.Integer, sa.ForeignKey('products.idProduct'), primary_key=True, nullable=False),
        sa.Column('idStore', sa.Integer, sa.ForeignKey('stores.idStore'), primary_key=True, nullable=False)
    )

def downgrade():
    op.drop_table('storeinventorys')
