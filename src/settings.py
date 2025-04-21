import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from src.constants import ENV_PATH


load_dotenv(ENV_PATH)


class PostgresSettings(BaseSettings):
    host: str = os.getenv("PG_HOST")
    port: int = os.getenv("PG_PORT")
    user: str = os.getenv("PG_USER")
    password: str = os.getenv("PG_PASSWORD")
    db: str = os.getenv("PG_DB")
    driver: str = "asyncpg"

    url: str = f"postgresql+{driver}://{user}:{password}@{host}:{port}/{db}"


class AuthSettings(BaseSettings):
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str =os.getenv("ALGORITHM")


class Settings(BaseSettings):
    auth: AuthSettings = AuthSettings()
    postgres: PostgresSettings = PostgresSettings()
