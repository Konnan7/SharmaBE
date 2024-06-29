from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import relationship
from models.base import Base

class Clubs(Base):
    __tablename__ = "clubs"

    club_id = Column(Integer, primary_key=True, autoincrement=True)
    schedules = Column(JSON, nullable=True)  # Assuming JSON for storing schedules
    location = Column(String, nullable=False)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)

    # Relationships
    users = relationship("Users", back_populates="pref_club")
    rates = relationship("Rates", back_populates="club")
