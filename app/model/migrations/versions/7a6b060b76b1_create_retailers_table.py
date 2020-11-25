"""Create Retailers Table

Revision ID: 7a6b060b76b1
Revises: f591f3ff5ef4
Create Date: 2020-11-24 14:53:28.931152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a6b060b76b1'
down_revision = 'f591f3ff5ef4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'retailers',
        sa.Column('idRetailer', sa.Integer, primary_key=True),
        sa.Column('Name', sa.String(45), nullable=False),
        sa.Column('Address', sa.String(45), nullable=False),
        sa.Column('idContact', sa.Integer, sa.ForeignKey("contacts.idContact")),
        sa.Column('idManufacturer', sa.Integer, sa.ForeignKey("manufacturers.idManufacturer"))
    )


def downgrade():
    op.drop_table('retailers')
