"""Create Cars Table

Revision ID: 7237c0f1abc8
Revises: 
Create Date: 2020-11-24 14:50:10.949053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7237c0f1abc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cars',
        sa.Column('idCar', sa.INTEGER, primary_key=True),
        sa.Column('Model', sa.String(45), nullable=False),
        sa.Column('ModelYear', sa.String(4), nullable=False),
        sa.Column('Color', sa.String(45), nullable=False),
        sa.Column('RegNumber', sa.String(32), nullable=False),

        sa.Column('idSource', sa.INTEGER, sa.ForeignKey('sources.idSource'), nullable=False),
        sa.Column('idCustomer', sa.INTEGER, sa.ForeignKey('customers.idCustomer'), nullable=False),
    )

def downgrade():
    op.drop_table('cars')
