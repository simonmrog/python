from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


# FastAPI instance
app = FastAPI()


# Using ENUM to use predetermined values in a path parameter
class ModelName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model": "alexnet model"}

    if model_name == ModelName.RESNET:
        return {"model": "resnet model"}

    if model_name == ModelName.LENET:
        return {"model": "lenet model"}


# Variable containing a path using Starlette
@app.get("/path/{file_path:path}")
async def get_path(file_path: str):
    return {"path": file_path}


# Query params
data = [
    {"item1": "value1"},
    {"item2": "value2"},
    {"item3": "value3"},
    {"item4": "value4"},
    {"item5": "value5"},
]


@app.get("/query_params/")
async def query_params(skip: int = 0, limit: int = 10):
    return data[skip : skip + limit]


# Request body and pydantic
class User(BaseModel):
    username: str
    password: str
    email: str


@app.post("/users")
async def create_user(user: User):
    return user
