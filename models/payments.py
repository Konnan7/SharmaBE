import datetime
from sqlalchemy import Column, Integer, Float, TIMESTAMP
from sqlalchemy.orm import relationship
from models.base import Base

class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    external_payment_id = Column(Integer, nullable=False)
    date_of_creation = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    # Relationships
    tickets = relationship("Tickets", back_populates="payment")
