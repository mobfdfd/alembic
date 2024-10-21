"""migration2

Revision ID: 2d289e429bdb
Revises: 0f4a08e3b99c
Create Date: 2024-05-21 23:57:51.841301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2d289e429bdb'
down_revision: Union[str, None] = '0f4a08e3b99c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'date_birth',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'date_birth',
               existing_type=sa.String(length=100),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    # ### end Alembic commands ###