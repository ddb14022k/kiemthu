"""empty message

Revision ID: 69e8cadb1198
Revises: 0c6590f323c1
Create Date: 2020-11-03 16:30:26.229996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69e8cadb1198'
down_revision = '0c6590f323c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.Enum('admin', 'member', name='userrole'), server_default='member', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
