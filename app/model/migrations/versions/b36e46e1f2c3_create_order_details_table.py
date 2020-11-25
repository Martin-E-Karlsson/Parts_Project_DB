"""Create Order_details Table

Revision ID: b36e46e1f2c3
Revises: 35cba7d29450
Create Date: 2020-11-24 14:52:17.342424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36e46e1f2c3'
down_revision = '35cba7d29450'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orderdetails',
        sa.Column('ProductQuantity', sa.Integer, nullable=False),
        sa.Column('PurchaseDate', sa.DATETIME, nullable=False),
        sa.Column('idOrder', sa.Integer, sa.ForeignKey('orders.idOrder'), primary_key=True, nullable=False),
        sa.Column('idProduct', sa.Integer, sa.ForeignKey('products.idProduct'), primary_key=True, nullable=False),
        sa.Column('idEmployee', sa.Integer, sa.ForeignKey('employees.idEmployee'), nullable=False)
    )


def downgrade():
    op.drop_table('orderdetails')
