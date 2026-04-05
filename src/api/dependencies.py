from typing import Annotated
from fastapi import Query, Depends
from pydantic import BaseModel
from utils.db_manager import DBManager
from src.database import async_session_maker
from src.services.family import FamilyService
from src.services.user import UserService

class PaginationParams(BaseModel):
    page:     Annotated[int | None, Query(1, ge = 1)]
    per_page: Annotated[int | None, Query(None, ge = 1, le = 30)]


PaginationDep = Annotated[PaginationParams, Depends()]


async def get_db():
      """Создает сессию"""
      async with DBManager(session_factory=async_session_maker) as db:
            yield db

def get_family_service(db: DBManager = Depends(get_db)):
    """Создает Family Service из репозиторие"""
    return FamilyService(family_repository=db.families, user_repository=db.users)

def get_user_service(db: DBManager = Depends(get_db)):
    """Создает User Service из репозиторие"""
    return UserService(user_repository=db.users)

DBDep = Annotated[DBManager, Depends(get_db)]
FamilyServiceDep = Annotated[FamilyService, Depends(get_family_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]

