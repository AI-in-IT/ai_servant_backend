from api.dependencies import PaginationDep
from fastapi import APIRouter, Body, Query
from src.schemas.users import UserAddRequest, UserPatchRequest
from api.dependencies import DBDep, UserServiceDep

router = APIRouter(prefix="/tasks", tags=["Задачи"])


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


