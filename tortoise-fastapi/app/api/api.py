from fastapi import APIRouter
from app.api.endpoints import city

router = APIRouter()

router.include_router(city.router, prefix="/cities")
