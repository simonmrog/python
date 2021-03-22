from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.api import router
from app.config import settings

app = FastAPI()
app.include_router(router, prefix="/api")
# register_tortoise(
#     app,
#     db_url="settings.POSTGRES_URL",
#     modules={"models": ["app.models"]},
#     generate_schema=True,
#     add_exception_handlers=True,
# )
