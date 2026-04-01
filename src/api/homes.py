from api.dependencies import PaginationDep
from fastapi import APIRouter, Body, Query
from src.database import async_session_maker
from src.repositories.homes import HomesRepository
from src.schemas.homes import HomePatchRequest, HomeAddRequest, HomeAdd
from src.services.key_generation import generate_key

router = APIRouter(prefix="/homes", tags=["Дома"])


@router.get("/", summary="Получение информации о всех домах")
async def get_all_homes():
    async with async_session_maker() as session:
        homes = await HomesRepository(session).get_all()
    return homes

@router.get("/{home_id}",summary="Получение дома по id")
async def get_home(home_id:int):
    async with async_session_maker() as session:
        homes = await HomesRepository(session).get_one_or_none(id=home_id)
    return homes

@router.delete("/{home_id}", summary="Удаление дома")
async def delete_home(home_id : int ):
    async with async_session_maker() as session:
        await HomesRepository(session).delete(id = home_id)
        await session.commit()
    return {"status" : "OK"}

@router.post("", summary="Добавление дома")
async def creat_hotel(home_data : HomeAddRequest = Body(openapi_examples={
    "1": {
        "summary": "Гагарина", "value":{
           "title" : "Гагарина 83",
           "active" : True 
        }},
    "2" : {
        "summary": "Спутник", "value":{
           "title" : "Дача",
           "active" : True 
    }
        }})):
    
    _home_data = HomeAdd(key = generate_key(), **home_data.model_dump())  
    async with async_session_maker() as session:
        hotel = await HomesRepository(session).add(_home_data)
        await session.commit()

    return {"status" : "OK", "data": hotel}


@router.patch("/{home_id}", summary="Частичное изменение дома")
async def patch_room(home_id:int, home_data:HomePatchRequest):
    async with async_session_maker() as session:
        await HomesRepository(session).edit(home_data,exclude_unset=True,id = home_id)
        await session.commit()
    return {"status" : "OK"}
