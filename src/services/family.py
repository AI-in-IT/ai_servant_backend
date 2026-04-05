from src.repositories.families import FamiliesRepository
from src.repositories.users import UsersRepository
from src.schemas.families import Family, FamilyAdd
from src.schemas.users import User
from src.utils.exception import (
    FamilyNotFoundError,
    FamilyFullError,
    UserNotFoundError,
    AlreadyInFamilyError, 
    NotInFamilyError,
    InvalidInviteCodeError
)


class FamilyService:
    """Сервис для работы с Семьей"""
    def __init__(self, family_repository: FamiliesRepository, user_repository: UsersRepository):
        self.family_repo = family_repository
        self.user_repo = user_repository
    
    async def _get_existing_family(self,family_id: int) -> Family:
        """Возвращает семью или кидает FamilyNotFoundError"""
        family = await self.family_repo.get_one_or_none(id=family_id)
        if not family:
            raise FamilyNotFoundError(f"Семья с таким ID не найдена")
        return family

    async def _get_member_count(self,family: Family) -> int:
        member_count = await self.user_repo.count_members_in_family(family.id)
        return member_count

    async def _check_family_is_not_full(self,family: Family) -> None:
        member_count = await self._get_member_count(family)
        if member_count >= family.max_members: 
            raise FamilyFullError(f"Семья с таким ID полностью заполнена")

    async def _get_existing_user(self,user_id: int) -> User:
        """Возвращает юзера или кидает UserNotFoundError"""
        user = await self.user_repo.get_one_or_none(id=user_id)
        if not user:
            raise UserNotFoundError(f"Пользователь с таким ID не найден")
        return user

    async def _check_users_in_family(self,user: User, family_id: int) -> None:
        """Выкидывает NotInFamilyError если юзер не в семье"""
        if user.family_id != family_id:
            raise NotInFamilyError(f"Пользователь с таким ID не состоит в этой семье")

    
    async def _check_users_not_in_family(self,user: User) -> None:
        """Выкидывает AlreadyInFamilyError если юзер уже состоит в семье"""
        if user.family_id:
            raise AlreadyInFamilyError(f"Пользователь с таким ID уже состоит в семье")


    async def create(self, data: FamilyAdd) -> Family:
        """Создает новую семью"""
        family = await self.family_repo.add(data)
        return family 
    
    async def delete(self, family_id: int) -> None:
        """Удаляет семью или говорит что ее не существует"""
        await self._get_existing_family(family_id)
        await self.family_repo.delete(id = family_id)


    async def add_member(self, family_id: int, family_key: str, user_id: int) -> None:
        family = await self._get_existing_family(family_id)
        
        if family.key != family_key:
            raise InvalidInviteCodeError(f"Неверный код для подключения к семье")
        else:
            user = await self._get_existing_user(user_id)
            await self._check_family_is_not_full(family)
            await self._check_users_not_in_family(user)
            await self.user_repo.set_family_id(user_id=user.id, family_id=family.id)
    
    async def remove_member(self, family_id: int, user_id: int) -> None:
        family = await self._get_existing_family(family_id)
        user = await self._get_existing_user(user_id)
        await self._check_users_in_family(family_id=family.id, user=user)
        await self.user_repo.set_family_id(user_id=user.id, family_id=None)

    async def get_family_by_key(self, family_key: str) -> Family:
        family = await self.family_repo.get_one_or_none(key=family_key)
        if family is None:
            raise InvalidInviteCodeError(f"Некорректный код подключения")
        return family


    
