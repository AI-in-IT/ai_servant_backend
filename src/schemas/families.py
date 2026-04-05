from pydantic import BaseModel, Field

class FamilyAddRequest(BaseModel):
    title: str
    active: bool

class FamilyAdd(FamilyAddRequest):
    key: str
    max_members: int = 2
class Family(FamilyAddRequest):
    id: int
    key: str
    max_members: int = 2

class FamilyJoinRequest(BaseModel):
    key: str



class FamilyPatchRequest(BaseModel):
    title: str | None = Field(None)
    active: bool | None = Field(None)
    max_members: int | None = Field(None)


