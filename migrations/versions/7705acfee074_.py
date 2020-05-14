"""empty message

Revision ID: 7705acfee074
Revises: 71bb195394dd
Create Date: 2020-05-14 04:09:57.703890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7705acfee074'
down_revision = '71bb195394dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todolists', 'done',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todolists', 'done',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
