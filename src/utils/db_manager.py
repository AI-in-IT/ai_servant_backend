from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.families import FamiliesRepository
from src.repositories.users import UsersRepository

class DBManager:
    """Класс для управления БД по патерну Unit of Work"""
    def __init__(self,session_factory):
        self.session_factory = session_factory
        self._is_commited: bool = False
        self.session: Optional[AsyncSession] = None
        self.families: Optional[FamiliesRepository] = None
        self.users: Optional[UsersRepository] = None


    async def __aenter__(self):
        self.session = self.session_factory()

        self.families = FamiliesRepository(self.session)
        self.users = UsersRepository(self.session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and not self._is_commited:
            await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
        self._is_commited = True