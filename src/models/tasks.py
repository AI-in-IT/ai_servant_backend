from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import String, ForeignKey,Boolean, Integer

from src.database import Base

class TasksOrm(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}
    
    id: Mapped[int] = mapped_column(primary_key = True)
    content: Mapped[str] = mapped_column(String(255))
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    owner_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=True, index=True)
    created_by_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True)
    cost: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[int] = mapped_column(Integer, default=1)
    
