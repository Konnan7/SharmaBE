import datetime
import os

from models.base import Base
from sqlalchemy import Column, Integer, TIMESTAMP, String, UniqueConstraint


class Usuarios(Base):
    __tablename__ = "usuarios"

    __table_args__ = (
        UniqueConstraint("phone_number", name="phone_number_unique"),
    )

    phone_prefix = Column(Integer, nullable=False, unique=True)
    phone_number = Column(Integer, nullable=False, unique=True)
    id = Column(Integer, primary_key=True)

    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

