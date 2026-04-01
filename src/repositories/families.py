from repositories.base import BaseRepository
from src.models.families import FamiliesOrm
from src.schemas.families import Family


class FamiliesRepository(BaseRepository):
    model = FamiliesOrm
    schema = Family

    
