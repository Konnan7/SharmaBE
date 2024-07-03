from models.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint

class Clubs(Base):
    __tablename__ = "clubs"

    club_id = Column(Integer, primary_key=True, autoincrement=True)
    schedule = Column(String, nullable=False)  # JSON or String depending on use case
    location = Column(String, nullable=False)  # Assuming GPS coordinates as string
    name = Column(String, nullable=False, unique=True)  # Unique constraint added
    status = Column(String, nullable=False)  # Active or Not active

    __table_args__ = (
        UniqueConstraint("name", name="club_name_unique"),
    )
