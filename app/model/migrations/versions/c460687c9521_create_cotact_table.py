"""Create Cotact Table

Revision ID: c460687c9521
Revises: 8264ee3d46e2
Create Date: 2020-11-24 14:50:53.521347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c460687c9521'
down_revision = '8264ee3d46e2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contacts',
        sa.Column('idContact', sa.Integer, primary_key=True),
        sa.Column('Name', sa.String(45), nullable=False),
        sa.Column('PhoneNumber', sa.String(45), nullable=False),
        sa.Column('Email', sa.String(45), nullable=False),
        sa.Column('idCompany', sa.Integer, sa.ForeignKey("companies.idCompany"))
    )

def downgrade():
    op.drop_table('contacts')
