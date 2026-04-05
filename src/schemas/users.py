from pydantic import BaseModel, Field

class UserAddRequest(BaseModel):
    tg_id: int
    name: str
    active: bool


class User(UserAddRequest):
    id: int
    family_id: int | None = Field(None)


class UserPatchRequest(BaseModel):
    name: str | None = Field(None)
    active: bool | None = Field(None)
    family_id: int | None = Field(None)


