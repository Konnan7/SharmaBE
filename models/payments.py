import datetime
from models.base import Base
from sqlalchemy import Column, Integer, Float, DateTime, UniqueConstraint, String


class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    amount = Column(Integer, nullable=False)
    currency = Column(String, nullable=False)
    stripe_id = Column(Integer, nullable=False, unique=True)  # Unique constraint added
    date_of_creation = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String, nullable=False)
    # source = Column(String, nullable=False)


    __table_args__ = (
        UniqueConstraint("payment_id", name="payment_id_unique"),
        UniqueConstraint("stripe_id", name="stripe_id_unique"),
    )
