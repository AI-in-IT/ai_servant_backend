from pydantic import BaseModel, Field

class TaskAddRequest(BaseModel):
    content: str
    created_by_id: int
    cost: int 
    status: int
    active: bool
    owner_id: int | None = Field(None)


class Task(TaskAddRequest):
    id: int



