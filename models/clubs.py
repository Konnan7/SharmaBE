from models.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint

class Clubs(Base):
    __tablename__ = "clubs"

    Club_id = Column(Integer, primary_key=True, autoincrement=True)
    Horarios = Column(String, nullable=False)  # JSON or String depending on use case
    Location = Column(String, nullable=False)  # Assuming GPS coordinates as string
    Name = Column(String, nullable=False, unique=True)  # Unique constraint added
    Status = Column(String, nullable=False)  # Active or Not active

    __table_args__ = (
        UniqueConstraint("Name", name="club_name_unique"),
    )
