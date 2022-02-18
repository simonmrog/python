import jwt
from passlib.hash import bcrypt
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models import UserAuth
from app.config import settings
from app.schemas.auth import UserAuthSchema, UserAuthInSchema
from app.services.auth import user_auth_service, oauth2_scheme

router = APIRouter()


@router.get("/me", response_model=UserAuthSchema)
async def get_users(user: UserAuth = Depends(user_auth_service.get_current_user)):
    return user


@router.post("/", response_model=UserAuthSchema)
async def create_user(user: UserAuthInSchema):
    user_obj = UserAuth(
        username=user.username, password_hash=bcrypt.hash(user.password_hash)
    )
    await user_obj.save()
    user = await UserAuthSchema.from_tortoise_orm(user_obj)
    return user
