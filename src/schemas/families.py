from pydantic import BaseModel, Field

class FamilyAddRequest(BaseModel):
    title: str
    active: bool

class FamilyAdd(FamilyAddRequest):
    key: str

class Family(FamilyAddRequest):
    id: int
    key: str


class FamilyPatchRequest(BaseModel):
    title: str | None = Field(None)
    active: bool | None = Field(None)


