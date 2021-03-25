from pydantic import BaseSettings, Field, AnyUrl


class Settings(BaseSettings):
    DEBUGGER: bool = Field(...)
    DATABASE_URL: AnyUrl = Field(...)
    JWT_SECRET: str = Field(...)


settings = Settings()
