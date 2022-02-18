from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database import retrieve_students

from app.models.student import StudentSchema, ResponseModel


router = APIRouter()


@router.get("/")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieve successfully")
    return ResponseModel(students, "Empty list")
