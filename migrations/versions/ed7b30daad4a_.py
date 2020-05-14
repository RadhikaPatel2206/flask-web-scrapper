"""empty message

Revision ID: ed7b30daad4a
Revises: 3871d7f9fffa
Create Date: 2020-05-14 17:46:12.420389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed7b30daad4a'
down_revision = '3871d7f9fffa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('searches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search', sa.String(length=500), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('search')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('search', sa.VARCHAR(length=500), nullable=True),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('searches')
    # ### end Alembic commands ###
