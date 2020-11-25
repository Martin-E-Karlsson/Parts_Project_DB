"""Create Costomers Table

Revision ID: efed3cbf5f3b
Revises: c460687c9521
Create Date: 2020-11-24 14:51:17.458446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efed3cbf5f3b'
down_revision = 'c460687c9521'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cars',
        sa.Column('idContact', sa.Integer, primary_key=True),
        sa.Column('Name', sa.String(45), nullable=False),
        sa.Column('PhoneNumber', sa.String(45), nullable=False),
        sa.Column('Email', sa.String(45), nullable=False),
        sa.Column('idCompany', sa.Integer, sa.ForeignKey("companies.idCompany"))
    )

def downgrade():
    op.drop_table('cars')
