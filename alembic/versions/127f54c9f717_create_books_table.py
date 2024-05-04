"""Create books table

Revision ID: 127f54c9f717
Revises: 
Create Date: 2024-05-04 12:11:12.300476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '127f54c9f717'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the books table
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('author', sa.String, nullable=False),
        sa.Column('year', sa.Integer),
        sa.Column('isbn', sa.String, nullable=False)
    )


def downgrade() -> None:
    # Drop the books table
    op.drop_table('books')