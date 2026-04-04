from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import String, ForeignKey,Boolean

from src.database import Base

class UsersOrm(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    
    id: Mapped[int] = mapped_column(primary_key = True)
    tg_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(200))
    active: Mapped[bool] = mapped_column(Boolean)
    family_id: Mapped[int | None] = mapped_column(
        ForeignKey("families.id", ondelete="SET NULL"),
        nullable=True, index=True)
    
    