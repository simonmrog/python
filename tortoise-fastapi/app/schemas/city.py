from app.models.city import City as CityModel
from tortoise.contrib.pydantic import pydantic_model_creator

CityOut = pydantic_model_creator(CityModel, name="City")
CityIn = pydantic_model_creator(CityModel, name="CityIn", exclude_readonly=True)
