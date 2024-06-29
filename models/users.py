import datetime
from sqlalchemy import Column, Integer, String, Date, Boolean, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from models.base import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    surname1 = Column(String, nullable=False)
    surname2 = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)  # Using String for phone number
    phone_prefix = Column(String, nullable=False)  # Using String for phone prefix
    foot_number = Column(Float, nullable=False)
    pref_club_id = Column(Integer, ForeignKey("clubs.club_id"), nullable=True)
    user_tickets = Column(String, nullable=True)  # You might want to use a relationship instead
    account_stripe_id = Column(String, nullable=True)
    reduced = Column(Boolean, default=False)
    end_reduced = Column(Date, nullable=True)

    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    # Relationships
    pref_club = relationship("Clubs", back_populates="users")
    tickets = relationship("Tickets", back_populates="user")
