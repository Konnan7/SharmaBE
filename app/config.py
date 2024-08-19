from pydantic import AnyUrl, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os

#Cargar variables de entorno
load_dotenv('.env-local')

STRIPE_SECRET_KEY=os.getenv("STRIPE_SECRET_KEY")



class Config(BaseSettings):
    postgres_host: PostgresDsn  # os.getenv("db_host")
    #redis_host: RedisDsn

    class Config:
        env_prefix = "db_"

