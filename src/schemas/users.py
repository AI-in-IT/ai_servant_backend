from pydantic import BaseModel, Field

class UserAddRequest(BaseModel):
    tg_id: int
    name: str
    active: bool

class User(UserAddRequest):
    id: int
    family: int | None = Field(None)


class UserPatchRequest(BaseModel):
    name: str | None = Field(None)
    active: bool | None = Field(None)
    family: int | None = Field(None)


