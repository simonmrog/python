from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator


# Defining pydantic model of User
class User(BaseModel):
    id: int
    username: str
    password: str
    password_confirm: str
    created_at: Optional[datetime] = None
    friends: List[int] = []

    @validator("password")
    def password_validator(cls, password):
        if len(password) < 8:
            raise Exception("Password must be longer than 8 characters")
            return None
        return password

    @validator("password_confirm")
    def passwords_match(cls, password_confirm, values):
        print(values)
        if "password" in values and password_confirm != values["password"]:
            raise Exception("Passwords do not match")
            return None
        return password_confirm


def use_pydantic():
    try:
        user_data = {
            "id": "12s542",
            "username": "simon",
            "password": "mypass123",
            "password_confirm": "mypass",
            "friends": [1, "2", 3],
        }

        user = User(**user_data)
        print(user)
    except Exception as e:
        print("[ERROR] ", e)


if __name__ == "__main__":
    use_pydantic()
