from pydantic import BaseModel, Field

class HomeAddRequest(BaseModel):
    title: str
    active: bool

class HomeAdd(HomeAddRequest):
    key: str

class Home(HomeAddRequest):
    id: int
    key: str


class HomePatchRequest(BaseModel):
    title: str | None = Field(None)
    active: bool | None = Field(None)


