from api.dependencies import PaginationDep
from fastapi import APIRouter, Body, Query
from src.database import async_session_maker
from src.repositories.families import FamiliesRepository
from src.schemas.families import Family, FamilyAdd, FamilyAddRequest, FamilyPatchRequest
from src.services.key_generation import generate_key
from api.dependencies import DBDep

router = APIRouter(prefix="/families", tags=["Семьи"])





@router.get("/", summary="Получение информации о всех семьях")
async def get_all_families(db: DBDep):
    families = await db.families.get_all()
    return families

@router.get("/{family_id}",summary="Получение семьи по id")
async def get_family(db: DBDep, family_id:int):
    family = await db.families.get_one_or_none(id=family_id)
    return family

@router.delete("/{family_id}", summary="Удаление семьи")
async def delete_family(db: DBDep, family_id : int ):
    await db.families.delete(id = family_id)
    await db.commit()
    return {"status" : "OK"}

@router.post("/", summary="Добавление семьи")
async def creat_family(db: DBDep,family_data : FamilyAddRequest = Body(openapi_examples={
    "1": {
        "summary": "Ивановы", "value":{
           "title" : "Ивановы",
           "active" : True 
        }},
    "2" : {
        "summary": "Сенькины", "value":{
           "title" : "Сенькины",
           "active" : True 
    }
        }})):
    
    _family_data = FamilyAdd(key = generate_key(), **family_data.model_dump())  
    family = await db.families.add(_family_data)
    await db.commit()

    return {"status" : "OK", "data": family}


@router.patch("/{family_id}", summary="Редактирование семьи")
async def patch_family(db: DBDep,family_id:int, family_data:FamilyPatchRequest):
    await db.families.edit(family_data,exclude_unset=True,id = family_id)
    await db.commit()
    return {"status" : "OK"}
