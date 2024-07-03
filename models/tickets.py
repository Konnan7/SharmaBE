import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Tickets(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)  # Unique constraint added
    status = Column(String, nullable=False)  # Activo, Utilizado
    date_of_creation = Column(DateTime, default=datetime.datetime.utcnow)
    qr_id = Column(String, nullable=False, unique=True)
    payment_id = Column(Integer, ForeignKey("payments.payment_id"), nullable=False, unique=True)
    rate_snapshot = Column(String, nullable=False)  # JSON format
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship("Users", back_populates="user_tickets")

    __table_args__ = (
        UniqueConstraint("ticket_id", name="ticket_id_unique"),
        UniqueConstraint("qr_id", name="qr_id_unique"),
    )
