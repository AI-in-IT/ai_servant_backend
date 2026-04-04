from repositories.base import BaseRepository
from src.models.users import UsersOrm
from src.schemas.users import User, UserPatchRequest
from sqlalchemy import func, select

class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    
async def count_members_in_family(self, family_id: int) -> int:
    """Возвращает точное количество участников в семье"""
    query = select(func.count(self.model.id)).where(self.model.family_id == family_id)
    result = await self.session.execute(query)
    return result.scalar_one()  

async def set_family_id(self, user_id: int, family_id: int | None) -> None:
    """Проставляет ID семьи или проставляет None"""
    data = UserPatchRequest(family_id=family_id)
    await self.edit(data=data, exclude_unset=True, id=user_id)