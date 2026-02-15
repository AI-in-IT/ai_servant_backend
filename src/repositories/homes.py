from repositories.base import BaseRepository
from src.models.homes import HomesOrm
from src.schemas.homes import Home


class HomesRepository(BaseRepository):
    model = HomesOrm
    schema = Home

    
