from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Пользователи"])


users = ["Андрей", "Люда"]


@router.get("/", summary="получение информации о всех пользователях")
async def get_all_users():
    users = users
    return users
