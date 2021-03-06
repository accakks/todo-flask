"""empty message

Revision ID: 81817de3e3c7
Revises: 4a59ee12b54a
Create Date: 2020-05-12 19:54:11.539441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81817de3e3c7'
down_revision = '4a59ee12b54a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todo', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todo', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
