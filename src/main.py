import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request

from fastapi.responses import JSONResponse
sys.path.append(str(Path(__file__).parent.parent))

from src.utils.exception import (
    DomainError,
    FamilyNotFoundError,
    FamilyFullError,
    AlreadyInFamilyError,
    UserNotFoundError,
    NotInFamilyError,
    InvalidInviteCodeError,
    UserAlreadyRegistrationError
)




from src.api.docs import create_docs_router
from src.api.family import router as router_families
from src.api.users import router as router_users
app = FastAPI(docs_url=None, redoc_url=None)

router_docs = create_docs_router(app)

app.include_router(router_docs)
app.include_router(router_families)
app.include_router(router_users)



# 🗺 Карта: Исключение → HTTP-статус
DOMAIN_ERROR_STATUS_MAP = {
    FamilyNotFoundError: 404,
    FamilyFullError: 409,
    AlreadyInFamilyError: 409,
    UserNotFoundError: 404,
    NotInFamilyError: 400,
    InvalidInviteCodeError: 400,
    UserAlreadyRegistrationError: 409
}

@app.exception_handler(DomainError)
async def domain_exception_handler(request: Request, exc: DomainError):
    status_code = DOMAIN_ERROR_STATUS_MAP.get(type(exc), 400)
    return JSONResponse(
        status_code=status_code,
        content={"detail": str(exc)},
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
