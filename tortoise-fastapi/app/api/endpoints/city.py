from fastapi import APIRouter
from app.models.city import City as CityModel
from app.schemas.city import CityIn, CityOut
import asyncio

router = APIRouter()


@router.get("/")
async def get_cities():
    cities = await CityOut.from_queryset(CityModel.all())
    tasks = []
    for city in cities:
        task = asyncio.create_task(CityModel.get_current_time(city))
        tasks.append(task)

    futures = [CityModel.get_current_time(city) for city in cities]
    await asyncio.gather(*futures)
    return cities


@router.get("/{city_id}")
async def get_city_by_id(city_id: int):
    city = await CityOut.from_queryset_single(CityModel.get(id=city_id))
    return city


@router.post("/")
async def create_city(city: CityIn):
    city = await CityModel.create(**city.dict(exclude_unset=True))
    city_out = await CityOut.from_tortoise_orm(city)
    return city_out


@router.delete("/")
async def delete_city(city_id: int):
    await CityModel.filter(id=city_id).delete()
    return True
