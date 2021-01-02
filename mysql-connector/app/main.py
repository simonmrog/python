from fastapi import FastAPI

from app.api.api import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/api")
    return app


app = create_app()
