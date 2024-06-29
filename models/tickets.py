import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Tickets(Base):
    __tablename__ = "tickets"

    Ticket_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)  # Unique constraint added
    Status = Column(String, nullable=False)  # Activo, Utilizado
    Date_of_creation = Column(DateTime, default=datetime.datetime.utcnow)
    Qr_id = Column(String, nullable=False, unique=True)
    Payment_id = Column(Integer, ForeignKey("payments.Payment_id"), nullable=False, unique=True)
    Rate_snapshot = Column(String, nullable=False)  # JSON format
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship("Users", back_populates="User_tickets")

    __table_args__ = (
        UniqueConstraint("Ticket_id", name="ticket_id_unique"),
        UniqueConstraint("Qr_id", name="qr_id_unique"),
    )
