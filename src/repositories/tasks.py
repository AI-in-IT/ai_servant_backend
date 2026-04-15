from repositories.base import BaseRepository
from src.models.tasks import TasksOrm
from src.schemas.tasks import Task, TaskAddRequest
from sqlalchemy import func, select, update

class TaskRepository(BaseRepository):
    model = TasksOrm
    schema = Task

    

    async def assign_task(self,task_id: int, owner_id: int) -> Task:
        stmt = (
        update(self.model)
        .where(self.model.id == task_id)
        .values(owner_id=owner_id)
        .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def change_status_task(self,task_id: int, status: int) -> Task:
        stmt = (
        update(self.model)
        .where(self.model.id == task_id)
        .values(status=status)
        .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    


