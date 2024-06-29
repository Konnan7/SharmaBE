import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from models.base import Base

class Tickets(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    date_of_creation = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    qr_id = Column(String, nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.payment_id"), nullable=False)
    rate_snapshot = Column(JSON, nullable=False)

    # Relationships
    user = relationship("Users", back_populates="tickets")
    payment = relationship("Payments", back_populates="tickets")
