"""rename password field

Revision ID: e4929a5c68fc
Revises: ba1e20d83f07
Create Date: 2024-08-03 22:07:35.995724

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e4929a5c68fc"
down_revision: Union[str, None] = "ba1e20d83f07"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("password_hashed", sa.String(length=256), nullable=False),
    )
    op.drop_column("users", "hashed_password")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "hashed_password",
            sa.VARCHAR(length=256),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_column("users", "password_hashed")
    # ### end Alembic commands ###