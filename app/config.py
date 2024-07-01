from pydantic import AnyUrl, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings



class Config(BaseSettings):
    postgres_host: PostgresDsn  # os.getenv("db_host")
    #redis_host: RedisDsn

    class Config:
        env_prefix = "db_"

