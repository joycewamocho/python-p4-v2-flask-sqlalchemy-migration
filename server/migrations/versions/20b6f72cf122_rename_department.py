"""rename department

Revision ID: 20b6f72cf122
Revises: 6a569d456e00
Create Date: 2025-01-15 16:38:22.823765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20b6f72cf122'
down_revision = '6a569d456e00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department','departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('departments','department')
    # ### end Alembic commands ###