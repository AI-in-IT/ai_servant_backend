import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.docs import create_docs_router
from src.api.family import router as router_families
from src.api.users import router as router_users
app = FastAPI(docs_url=None, redoc_url=None)

router_docs = create_docs_router(app)

app.include_router(router_docs)
app.include_router(router_families)
app.include_router(router_users)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
