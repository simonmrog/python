import os
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get(
    "/get_file/{filename}",
    responses={
        200: {
            "description": "Returns a file",
            "content": {"text/plain": {"example": "(no example available)"}},
        }
    },
)
def get_file(filename: str) -> Optional[FileResponse]:
    current_workdir = os.path.abspath(os.getcwd())
    file_path = os.path.join(current_workdir, filename)
    print(file_path)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/plain")
    else:
        return {"status": "error", "detail": "File not found"}
