"""Shopify store schema fixes

Revision ID: 364c42ad7d8e
Revises: f8a6ff4dc0b1
Create Date: 2024-04-14 19:02:31.989634

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = "364c42ad7d8e"
down_revision: Union[str, None] = "f8a6ff4dc0b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("shopify_pages", "email")
    op.drop_column("shopify_pages", "page_id")
    op.drop_column("shopify_pages", "shopify_store_id")

    op.add_column(
        "shopify_pages",
        sa.Column("page_id", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "shopify_pages",
        sa.Column(
            "shopify_store_id", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "shopify_pages",
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    # ### end Alembic commands ###
