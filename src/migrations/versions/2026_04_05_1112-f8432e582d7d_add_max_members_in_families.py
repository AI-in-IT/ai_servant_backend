"""add max_members in families

Revision ID: f8432e582d7d
Revises: 1fa1a729a94d
Create Date: 2026-04-05 11:12:56.197515

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "f8432e582d7d"
down_revision: Union[str, Sequence[str], None] = "1fa1a729a94d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "families",
        sa.Column("max_members", sa.Integer(), server_default="2", nullable=False),
    )
    op.add_column("users", sa.Column("family_id", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_users_family_id"), "users", ["family_id"], unique=False)
    op.drop_constraint(op.f("users_family_fkey"), "users", type_="foreignkey")
    op.create_foreign_key(
        None, "users", "families", ["family_id"], ["id"], ondelete="SET NULL"
    )
    op.drop_column("users", "family")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users", sa.Column("family", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.drop_constraint(None, "users", type_="foreignkey")
    op.create_foreign_key(
        op.f("users_family_fkey"),
        "users",
        "families",
        ["family"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_index(op.f("ix_users_family_id"), table_name="users")
    op.drop_column("users", "family_id")
    op.drop_column("families", "max_members")
