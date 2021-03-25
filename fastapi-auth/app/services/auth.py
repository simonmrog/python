import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.config import settings
from app.schemas.auth import UserAuthSchema
from app.models import UserAuth


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/access-token")


class UserAuthService:

    async def auth_user(self, *, username: str, password: str):
        try:
            user = await UserAuth.get(username=username)
            if not user:
                return False
            if not user.verify_password(password):
                return False
            return user
        except Exception as e:
            print(f"{e}")
            return False

    async def get_current_user(self, *, token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET, algorithms=["HS256"])
            user = await UserAuth.get(id=payload.get("id"))
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        return await UserAuthSchema.from_tortoise_orm(user)


user_auth_service = UserAuthService()
