from api.dependencies import PaginationDep
from fastapi import APIRouter, Body, Query
from src.schemas.users import UserAddRequest, UserPatchRequest
from api.dependencies import DBDep, UserServiceDep

router = APIRouter(prefix="/users", tags=["Пользователи"])

# Старые общие ручки 
# ----------------------------------------------------------------

# @router.get("/", summary="Получение всех пользователей")
# async def get_all_users(db: DBDep):
#     users = await db.users.get_all()
#     return users

# @router.get("/{user_id}", summary="Получение пользователя по ID")
# async def get_user(db:DBDep, user_id: int):
#     user = await db.users.get_one_or_none(id=user_id)
#     return user

# @router.get("/families/{family_id}", summary="Получение всех пользователей семьи по ее ID")
# async def get_user(db:DBDep, family_id: int):
#     users = await db.users.get_filtered(family = family_id)
#     return users

# @router.post("/", summary="Создание пользователя")
# async def reg_user(db: DBDep, user_data : UserAddRequest = Body(openapi_examples={
#     "1": {
#         "summary": "Андрей", "value":{
#             "tg_id": 123,
#             "name": "Иванов Андрей",
#             "active": True
#         }},
#     "2" : {
#         "summary": "Люда", "value":{
#             "tg_id": 456,
#             "name": "Иванова Людмила",
#             "active": True
#         }
#         }})):
    
#     user = await db.users.add(user_data)
#     await db.commit()
#     return{"status": "OK", "data": user}


# @router.delete("/{user_id}", summary= "Удаление пользователя по ID")
# async def delete_user(db:DBDep, user_id: int):
#     await db.users.delete(id=user_id)
#     await db.commit()
#     return {"status":"OK"}

# @router.patch("/{user_id}", summary="Редактирование пользователя по ID")
# async def edit_user(db:DBDep, user_id: int, user_data: UserPatchRequest):
#     user = await db.users.edit(user_data,exclude_unset=True,id = user_id)
#     await db.commit()
#     return {"status":"OK"}

# ----------------------------------------------------------------


# Новые спец ручки 
# ----------------------------------------------------------------

@router.get("/{user_tg_id}", summary="Получение пользователя по tg_id")
async def get_user(service: UserServiceDep, user_tg_id: int):
    user = await service.get_info_by_tg_id(tg_id=user_tg_id)
    return {"status": "OK", "data": user}


@router.post("/registration", summary="Регистрация пользователя")
async def registration_user(db: DBDep, servce: UserServiceDep, user_data: UserAddRequest):
    user = await servce.registration(user_data)
    await db.commit()
    return {"status": "OK", "data": user}

@router.delete("/unregistration/{tg_id}", summary="Удаление пользователя")
async def unregistration_user(db: DBDep, servce: UserServiceDep, tg_id: int):
    await servce.delete(tg_id=tg_id)
    await db.commit()
    return {"status": "OK"}


# ----------------------------------------------------------------