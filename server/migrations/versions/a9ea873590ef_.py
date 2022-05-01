"""empty message

Revision ID: a9ea873590ef
Revises: 603ec7635a3b
Create Date: 2020-11-12 23:32:39.466926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9ea873590ef'
down_revision = '603ec7635a3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_content', sa.Column('content', sa.JSON(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_content', 'content')
    # ### end Alembic commands ###
