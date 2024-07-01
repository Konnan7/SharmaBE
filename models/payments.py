import datetime
from models.base import Base
from sqlalchemy import Column, Integer, Float, DateTime, UniqueConstraint

class Payments(Base):
    __tablename__ = "payments"

    Payment_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    Price = Column(Float, nullable=False)
    Tax = Column(Float, nullable=False)
    External_payment_id = Column(Integer, nullable=False, unique=True)  # Unique constraint added
    Date_of_creation = Column(DateTime, default=datetime.datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("Payment_id", name="payment_id_unique"),
        UniqueConstraint("External_payment_id", name="external_payment_id_unique"),
    )
