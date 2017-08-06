"""init

Revision ID: bb695e1ec311
Revises: 
Create Date: 2017-08-06 17:49:02.060403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb695e1ec311'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('avator', sa.String(length=35), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('avator'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_User_email'), 'User', ['email'], unique=True)
    op.create_table('picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dsepriction', sa.String(length=5000), nullable=True),
    sa.Column('address', sa.String(length=35), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('dsepriction')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=50), nullable=True),
    sa.Column('picId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['picId'], ['picture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('picture')
    op.drop_index(op.f('ix_User_email'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###