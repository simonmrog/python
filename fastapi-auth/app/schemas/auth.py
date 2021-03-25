from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import UserAuth

UserAuthSchema = pydantic_model_creator(UserAuth, name="UserAuth")
UserAuthInSchema = pydantic_model_creator(
    UserAuth, name="UserAuthIn", exclude_readonly=True)
