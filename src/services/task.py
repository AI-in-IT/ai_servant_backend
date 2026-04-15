from src.repositories.tasks import TaskRepository
from src.repositories.users import UsersRepository
from src.schemas.tasks import Task, TaskAddRequest
from src.utils.exception import (
    UserNotFoundError,
    TaskNotFoundError
)


class TaskService:
    """Сервис для работы с задачами"""
    def __init__(self, task_repository: TaskRepository, user_repository: UsersRepository):
        self.task_repo = task_repository
        self.user_repo = user_repository

    async def _check_owner_exist(self, owner_id: int) -> None:
        """Проверка есть ли пользователь с таким ID в базе"""
        user = await self.user_repo.get_one_or_none(id=owner_id)
        if user is None:
            raise UserNotFoundError(f"Пользователь с таким ID не найден")

    async def _check_task_exist(self, task_id: int) -> None:
        """Проверка есть ли задача с таким ID в базе"""
        task = await self.task_repo.get_one_or_none(id=task_id)
        if task is None:
            raise TaskNotFoundError(f"задача с таким ID не найдена")

    async def add_task(self,data: TaskAddRequest) -> Task:
        """Создаем задачу в БД"""
        if data.owner is not None:
            await self._check_owner_exist(owner_id=data.owner_id)
        task = await self.task_repo.add(data)
        return task

    async def delete_task(self,task_id: int):
        """Удаляем задачу из БД"""
        await self._check_task_exist(task_id=task_id)
        await self.task_repo.delete(id=task_id)
        return 
    
    async def assign_task(self,task_id: int, owner_id) -> Task:
        """Назначить задачу существующему пользователю"""
        await self._check_task_exist(task_id=task_id)
        await self._check_owner_exist(owner_id=owner_id)
        task = await self.task_repo.assign_task(task_id,owner_id)
        return task

    async def change_status_task(self,task_id: int, status: int) -> Task:
        """Поменять статус задаче"""
        await self._check_task_exist(task_id=task_id)
        task = await self.task_repo.change_status_task(task_id=task_id, status=status)
        return task
 


