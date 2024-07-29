import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)  # Unique constraint added
    name = Column(String, nullable=False)
    surname1 = Column(String, nullable=False)
    surname2 = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    phone_prefix = Column(String, nullable=False)
    foot_number = Column(Float, nullable=True)
    pref_club_id = Column(Integer, ForeignKey("clubs.club_id"))
    # user_tickets = relationship("Tickets", back_populates="user")
    account_stripe_id = Column(String, nullable=True, unique=True)
    reduced = Column(Boolean, default=False)
    end_reduced = Column(Date, nullable=True)
    hashed_password = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", name="user_id_unique"),
        UniqueConstraint("email", name="email_unique"),
        UniqueConstraint("phone_number", name="phone_number_unique"),
        # UniqueConstraint("phone_prefix", name="phone_prefix_unique"),
        UniqueConstraint("account_stripe_id", name="account_stripe_id_unique"),
    )
