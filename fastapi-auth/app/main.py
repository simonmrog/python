from fastapi import FastAPI

from app.api.api import router
from app.db import init_db
from app.debugger import init_debugger

from app.config import settings


def init_app():
    app = FastAPI()
    if settings.DEBUGGER:
        init_debugger()
    app.include_router(router, prefix="/api")
    return app


app = init_app()


@app.on_event("startup")
async def startup_event():
    init_db(app)
