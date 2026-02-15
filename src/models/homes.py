from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import String,Boolean

from src.database import Base

class HomesOrm(Base):
    __tablename__ = "homes"
    __table_args__ = {'extend_existing': True}
    
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(200))
    key: Mapped[str] = mapped_column(
        String(64), 
        unique=True,  
        nullable=False
    )
    active: Mapped[bool] = mapped_column(Boolean)