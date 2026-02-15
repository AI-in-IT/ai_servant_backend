from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import String, ForeignKey, Date

from src.database import Base

class FoodsOrm(Base):
    __tablename__ = "foods"
    __table_args__ = {'extend_existing': True}
    
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(200))
    preparation_date: Mapped[date] = mapped_column(Date)
    expiration_date: Mapped[date] = mapped_column(Date)
    cooked_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    