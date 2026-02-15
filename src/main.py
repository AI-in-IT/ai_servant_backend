import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.docs import create_docs_router
from src.api.homes import router as router_homes
app = FastAPI(docs_url=None, redoc_url=None)

router_docs = create_docs_router(app)

app.include_router(router_docs)
app.include_router(router_homes)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
