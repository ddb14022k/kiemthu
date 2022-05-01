"""empty message

Revision ID: 98af07975445
Revises: 01b8b5d3f83f
Create Date: 2020-11-10 17:58:35.164729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98af07975445'
down_revision = '01b8b5d3f83f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_content', sa.Column('input_attrs', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_content', 'input_attrs')
    # ### end Alembic commands ###