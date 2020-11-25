"""Create Company Table

Revision ID: 8264ee3d46e2
Revises: 7237c0f1abc8
Create Date: 2020-11-24 14:50:38.020757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8264ee3d46e2'
down_revision = '7237c0f1abc8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'companies',
        sa.Column('idCompany', sa.Integer, primary_key=True),
        sa.Column('CompanyName', sa.String(45), nullable=False)
    )

def downgrade():
    op.drop_table('companies')
