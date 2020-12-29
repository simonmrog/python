from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()

@app.get("/")
async def hello(settings: Settings = Depends(get_settings)):
  return {
    "message": "Hello World!!!",
    "environment": settings.environment,
    "testing": settings.testing
  };
