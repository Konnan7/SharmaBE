from models.base import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, UniqueConstraint

class Rates(Base):
    __tablename__ = "rates"

    Rate_id = Column(Integer, primary_key=True, autoincrement=True)
    Price = Column(Float, nullable=False)
    Club_id = Column(Integer, ForeignKey("clubs.Club_id"), nullable=False)
    Type = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("Rate_id", name="rate_id_unique"),
    )
