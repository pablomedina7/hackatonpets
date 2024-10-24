"""empty message

Revision ID: 660f10474fb5
Revises: 
Create Date: 2024-10-24 14:15:39.979291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660f10474fb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mascotas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('fecha_adopcion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mascotas')
    # ### end Alembic commands ###