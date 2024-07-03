import datetime
from models.base import Base
from sqlalchemy import Column, Integer, Float, DateTime, UniqueConstraint

class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    external_payment_id = Column(Integer, nullable=False, unique=True)  # Unique constraint added
    date_of_creation = Column(DateTime, default=datetime.datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("payment_id", name="payment_id_unique"),
        UniqueConstraint("external_payment_id", name="external_payment_id_unique"),
    )
