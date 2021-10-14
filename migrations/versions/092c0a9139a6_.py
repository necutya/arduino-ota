"""empty message

Revision ID: 092c0a9139a6
Revises: 
Create Date: 2021-03-02 19:09:58.070731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '092c0a9139a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('second_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('group', sa.String(length=5), nullable=True),
    sa.Column('role', sa.Enum('teacher', 'student', name='userroleenum'), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###