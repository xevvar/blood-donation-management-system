"""Added Donor model

Revision ID: b1c77b2f230a
Revises: 34c1dfd973b9
Create Date: 2024-02-20 22:23:56.454303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1c77b2f230a'
down_revision: Union[str, None] = '34c1dfd973b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('blood_type', sa.String(length=3), nullable=True),
    sa.Column('allergies', sa.String(length=3), nullable=True),
    sa.Column('diseases', sa.String(length=3), nullable=True),
    sa.Column('contact_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donors')
    # ### end Alembic commands ###