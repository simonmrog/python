from fastapi import FastAPI

from app.routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, prefix="/students", tags=["Students"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
