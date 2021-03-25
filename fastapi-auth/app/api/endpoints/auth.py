import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import UserAuthSchema
from app.services.auth import user_auth_service
from app.config import settings


router = APIRouter()


@router.post("/access-token")
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await user_auth_service.auth_user(
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        return {"error": "Invalid credentials"}
    user_obj = await UserAuthSchema.from_tortoise_orm(user)
    token = jwt.encode(user_obj.dict(), settings.JWT_SECRET)
    return {"access_token": token, "token_type": "bearer"}
