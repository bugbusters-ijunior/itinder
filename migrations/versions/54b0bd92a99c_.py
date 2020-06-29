"""empty message

Revision ID: 54b0bd92a99c
Revises: f76d91bb591a
Create Date: 2020-06-29 14:20:14.786511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54b0bd92a99c'
down_revision = 'f76d91bb591a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('trainees')
    op.add_column('association', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint(None, 'association', type_='foreignkey')
    op.create_foreign_key(None, 'association', 'users', ['user_id'], ['id'])
    op.drop_column('association', 'trainee_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('association', sa.Column('trainee_id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'association', type_='foreignkey')
    op.create_foreign_key(None, 'association', 'trainees', ['trainee_id'], ['id'])
    op.drop_column('association', 'user_id')
    op.create_table('trainees',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('senha', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
