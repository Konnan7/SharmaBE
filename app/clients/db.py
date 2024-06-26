
from typing import Optional, Union
import os

from databases import Database
from app.config import Config
from sqlalchemy import create_engine, MetaData

from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Select, Delete, Insert


class DatabaseClient:
    def __init__(self, config: Config, tables: Optional[list[str]]):
        self.config = config  # import the config
        self.engine = create_engine(str(self.config.postgres_host), future=True)  # using the postgres_host of our config
        self.session = Session(bind=self.engine, future=True)  # starting a session in the DB
        self.metadata = MetaData()  # metadata.tables["user"]
        self.metadata.bind = self.engine
        self._reflect_metadata()
        if tables:
            self._set_internal_database_tables(tables)

        if os.getenv("app_env") == "test":
            self.database = Database(str(self.config.postgres_host), force_rollback=True)

        else:
            self.database = Database(str(self.config.postgres_host))

    async def get_first(self, query: Union[Select, Insert]) -> Optional[Row]:
        async with self.database.transaction():
            res = await self.database.fetch_one(query)
        return res

    def _reflect_metadata(self) -> None:
        self.metadata.reflect(self.engine)

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        await self.database.disconnect()

    def _set_internal_database_tables(self, tables: list[str]):
        for table in tables:
            setattr(self, table, self.metadata.tables[table])




