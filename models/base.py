import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, URL
from sqlalchemy.engine import URL, create

from app.config import Config
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

Base = declarative_base()
logging.debug(f"Starting configurations")

config = Config()
logging.debug(f"Using config field: {config}")


engine = create_engine(str(config.postgres_host), echo=True)


def recreate_postgres_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
