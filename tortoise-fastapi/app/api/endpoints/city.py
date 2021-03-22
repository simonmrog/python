from fastapi import APIRouter
from app.schemas.city import City
from app.db import cities

router = APIRouter()


@router.get("/")
def get_cities():
    return {"status": "ok", "data": cities}


@router.get("/{city_id}")
def get_city_by_id(city_id: int):
    return {
        "status": "ok",
        "data": cities[city_id - 1]
    }


@router.post("/")
def create_city(city: City):
    new_city = city.dict()
    cities.append(new_city)
    return {"status": "ok"}


@router.delete("/")
def delete_city(city_id: int):
    cities.pop(city_id - 1)
    return {"status": "ok", "data": cities}
