"""Added the comments class plus all the columns

Revision ID: 042d79677861
Revises: 72f59c0aebaa
Create Date: 2022-03-10 21:24:25.495201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042d79677861'
down_revision = '72f59c0aebaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_txt', sa.String(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###