from src.repositories.users import UsersRepository
from src.schemas.users import User, UserAddRequest
from src.utils.exception import (
    UserNotFoundError,
    UserAlreadyRegistrationError
)


class UserService:
    """Сервис для работы с пользователями"""
    def __init__(self, user_repository: UsersRepository):
        self.user_repo = user_repository

    async def _check_user_exist(self, tg_id) -> None:
        """Проверка есть ли пользователь с таким ID в базе"""
        user = await self.user_repo.get_one_or_none(tg_id=tg_id)

        if user is None:
            raise UserNotFoundError(f"Пользователь с таким ID не найден")


    async def _check_user_un_exist(self, tg_id) -> None:
        """Проверка нет ли пользователя с таким tg_id в базе"""
        user = await self.user_repo.get_one_or_none(tg_id=tg_id)

        if user is not None:
            raise UserAlreadyRegistrationError(f"Пользователь уже зарегистрирован")


    async def registration(self, data: UserAddRequest) -> User:
        """Регистрируем пользователя и добавляем его в БД"""
        await self._check_user_un_exist(tg_id=data.tg_id)
        user = await self.user_repo.add(data)
        return user
    
    async def delete(self,tg_id):
        """Удаляем пользователя из БД"""
        await self._check_user_exist(tg_id=tg_id)
        await self.user_repo.delete(tg_id=tg_id)
        return 

    async def get_info_by_tg_id(self,tg_id) -> User:
        """Получаем информацию о пользователе по его tg_id"""
        await self._check_user_exist(tg_id=tg_id)
        user = await self.user_repo.get_one_or_none(tg_id=tg_id)
        return user

