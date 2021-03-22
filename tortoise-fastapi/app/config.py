from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ENVIRONMENT: str
    TESTING: bool
    POSTGRES_URL: str


settings = Settings()
