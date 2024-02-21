"""Added Association table

Revision ID: 027c1b80056d
Revises: 092a10f4de84
Create Date: 2024-02-21 01:06:45.820123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '027c1b80056d'
down_revision: Union[str, None] = '092a10f4de84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association',
    sa.Column('donor_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['donor_id'], ['donors.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['receivers.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    # ### end Alembic commands ###
