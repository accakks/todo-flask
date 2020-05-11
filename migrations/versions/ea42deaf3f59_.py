"""empty message

Revision ID: ea42deaf3f59
Revises: 24ea4cd0ee72
Create Date: 2020-05-11 18:50:44.523476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea42deaf3f59'
down_revision = '24ea4cd0ee72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###
    op.execute('UPDATE todo SET completed = False WHERE completed is NULL;')
    op.alter_column('todo', 'completed', nullable=False)
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'completed')
    # ### end Alembic commands ###
