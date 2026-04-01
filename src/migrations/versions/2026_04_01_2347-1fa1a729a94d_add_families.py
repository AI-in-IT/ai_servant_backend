"""add families

Revision ID: 1fa1a729a94d
Revises: c748994e20bb
Create Date: 2026-04-01 23:47:22.822004

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "1fa1a729a94d"
down_revision: Union[str, Sequence[str], None] = "c748994e20bb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "families",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("key", sa.String(length=64), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    op.add_column("users", sa.Column("family", sa.Integer(), nullable=True))
    op.drop_constraint(op.f("users_home_fkey"), "users", type_="foreignkey")
    op.create_foreign_key(
        None, "users", "families", ["family"], ["id"], ondelete="SET NULL"
    )
    op.drop_column("users", "home")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users", sa.Column("home", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.drop_constraint(None, "users", type_="foreignkey")
    op.create_foreign_key(
        op.f("users_home_fkey"), "users", "homes", ["home"], ["id"], ondelete="SET NULL"
    )
    op.drop_column("users", "family")
    op.drop_table("families")
