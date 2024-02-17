"""Initial Migrations

Revision ID: 851aa60aa5c0
Revises: 
Create Date: 2024-02-18 03:49:18.605759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851aa60aa5c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_color', sa.String(length=200), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('favorite_color')

    # ### end Alembic commands ###