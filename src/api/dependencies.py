from typing import Annotated
from fastapi import Query, Depends
from pydantic import BaseModel
from utils.db_manager import DBManager
from src.database import async_session_maker
from src.services.family import FamilyService
from src.repositories.families import FamiliesRepository
from src.repositories.users import UsersRepository

class PaginationParams(BaseModel):
    page:     Annotated[int | None, Query(1, ge = 1)]
    per_page: Annotated[int | None, Query(None, ge = 1, le = 30)]


PaginationDep = Annotated[PaginationParams, Depends()]


async def get_db():
      async with DBManager(session_factory=async_session_maker) as db:
            yield db

DBDep = Annotated[DBManager, Depends(get_db)]


#def get_family_service(
#    session: AsyncSession = Depends(get_async_session),
#) -> FamilyService:
#    """Автоматически создаёт сервис с нужными репозиториями и сессией"""
#    return FamilyService(
#        family_repository=FamiliesRepository(session),
#        user_repository=UsersRepository(session)
#    )