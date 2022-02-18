from fastapi import APIRouter

from app.api.endpoints import root, employees

router = APIRouter()
router.include_router(root.router)
router.include_router(employees.router, prefix="/employees", tags=["employees"])
