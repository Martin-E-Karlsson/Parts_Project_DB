"""Create Orders Table

Revision ID: 35cba7d29450
Revises: 35d4ad3f9b29
Create Date: 2020-11-24 14:52:02.139464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35cba7d29450'
down_revision = '35d4ad3f9b29'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('idOrder', sa.Integer, primary_key=True),
        sa.Column('idCustomer', sa.Integer, sa.ForeignKey("customers.idCustomer"))
    )


def downgrade():
    op.drop_table('orders')
