from models.base import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, UniqueConstraint


class Rates(Base):
    __tablename__ = "rates"

    rate_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    club_id = Column(Integer, ForeignKey("clubs.club_id"), nullable=False)
    type = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("rate_id", name="rate_id_unique"),
    )
