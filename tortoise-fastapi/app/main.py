from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.api import router
from app.config import settings
from app.services.aiohttp import http_client

app = FastAPI()

app.include_router(router, prefix="/api")

register_tortoise(
    app,
    db_url=settings.POSTGRES_URL,
    modules={"models": ["app.models.city"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event("startup")
async def startup_event():
    http_client.start()


@app.on_event("shutdown")
async def shutdown_event():
    await http_client.stop()
