from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Rates(Base):
    __tablename__ = "rates"

    rate_id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    club_id = Column(Integer, ForeignKey("clubs.club_id"), nullable=False)
    type = Column(String, nullable=False)

    # Relationships
    club = relationship("Clubs", back_populates="rates")
