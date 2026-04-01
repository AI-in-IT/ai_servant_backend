from typing import Annotated
from fastapi import Query, Depends
from pydantic import BaseModel
from utils.db_manager import DBManager
from src.database import async_session_maker

class PaginationParams(BaseModel):
    page:     Annotated[int | None, Query(1, ge = 1)]
    per_page: Annotated[int | None, Query(None, ge = 1, le = 30)]


PaginationDep = Annotated[PaginationParams, Depends()]


async def get_db():
      async with DBManager(session_factory=async_session_maker) as db:
            yield db

DBDep = Annotated[DBManager, Depends(get_db)]