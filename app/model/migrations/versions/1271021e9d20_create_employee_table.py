"""Create Employee Table

Revision ID: 1271021e9d20
Revises: efed3cbf5f3b
Create Date: 2020-11-24 14:51:32.077530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1271021e9d20'
down_revision = 'efed3cbf5f3b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employees',
        sa.Column('idEmployee', sa.Integer, primary_key=True, nullable=False),
        sa.Column('Name', sa.String(100), nullable=False),
        sa.Column('Email', sa.String(100), nullable=False),
        sa.Column('PhoneNumber', sa.String(100), nullable=False),
        sa.Column('idStore', sa.Integer, sa.ForeignKey("stores.idStore"), nullable=False)
    )

def downgrade():
    op.drop_table('employees')
