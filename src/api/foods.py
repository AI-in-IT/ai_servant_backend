from fastapi import APIRouter

router = APIRouter(prefix="/foods", tags=["Готовая еда"])


food = ["фарш", "макароны"]


@router.get("/", summary="получение информации о всей готовой еде")
async def get_all_foods():
    foods = food
    return foods
