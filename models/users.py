import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)  # Unique constraint added
    Name = Column(String, nullable=False)
    Surname1 = Column(String, nullable=False)
    Surname2 = Column(String, nullable=True)
    Date_of_birth = Column(Date, nullable=False)
    Email = Column(String, nullable=False, unique=True)
    Phone_number = Column(String, nullable=False, unique=True)
    Phone_prefix = Column(String, nullable=False)
    Foot_number = Column(Float, nullable=True)
    Pref_club_id = Column(Integer, ForeignKey("clubs.Club_id"))
    User_tickets = relationship("Tickets", back_populates="user")
    Account_stripe_id = Column(String, nullable=True, unique=True)
    Reduced = Column(Boolean, default=False)
    End_reduced = Column(Date, nullable=True)

    __table_args__ = (
        UniqueConstraint("user_id", name="user_id_unique"),
        UniqueConstraint("Email", name="email_unique"),
        UniqueConstraint("Phone_number", name="phone_number_unique"),
        UniqueConstraint("Phone_prefix", name="phone_prefix_unique"),
        UniqueConstraint("Account_stripe_id", name="account_stripe_id_unique"),
    )
