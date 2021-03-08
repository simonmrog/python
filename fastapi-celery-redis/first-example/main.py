from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.workers.calc import multiply_numbers

app = FastAPI()


class Numbers(BaseModel):
    x: float
    y: float


@app.post("/multiply")
def multiply(n: Numbers):
    task = multiply_numbers.delay(n.x, n.y)
    result = task.get()
    return JSONResponse(content={"status": "ok", "data": result})
