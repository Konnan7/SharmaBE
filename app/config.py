import os
from pydantic import AnyUrl, PostgresDsn, RedisDsn, BaseSettings
from pydantic_settings import BaseSettings
from sqlalchemy import URL
import redis


class Config(BaseSettings):
    postgres_host: PostgresDsn  # os.getenv("db_host")
    redis_host: RedisDsn

    class Config:
        env_prefix = "db_"

