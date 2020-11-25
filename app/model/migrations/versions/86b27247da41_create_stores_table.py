"""Create Stores Table

Revision ID: 86b27247da41
Revises: 73f42c05c956
Create Date: 2020-11-24 14:53:56.565255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86b27247da41'
down_revision = '73f42c05c956'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stores',
        sa.Column('idStore', sa.Integer, primary_key=True, nullable=False),
        sa.Column('Name', sa.String(100), nullable=False),
        sa.Column('StoreType', sa.String(100), nullable=False)
    )


def downgrade():
    op.drop_table('stores')
