"""empty message

Revision ID: 322e0a190fe0
Revises: 
Create Date: 2024-10-24 14:33:43.115102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '322e0a190fe0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alimentacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mascota_id', sa.Integer(), nullable=False),
    sa.Column('fecha_alimentacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alimentacion')
    # ### end Alembic commands ###