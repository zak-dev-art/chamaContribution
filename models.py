from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base, engine

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)

    contributions = relationship("Contribution", back_populates="member")

    def __repr__(self):
        return f"<Member(id={self.id}, name='{self.name}')>"

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True)
    agenda = Column(String)
    meeting_date = Column(DateTime, default=datetime.utcnow)

    contributions = relationship("Contribution", back_populates="meeting")

    def __repr__(self):
        return f"<Meeting(id={self.id}, agenda='{self.agenda}')>"

class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    meeting_id = Column(Integer, ForeignKey("meetings.id"))
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    member = relationship("Member", back_populates="contributions")
    meeting = relationship("Meeting", back_populates="contributions")

    def __repr__(self):
        return f"<Contribution(member={self.member_id}, amount={self.amount})>"

# Create tables
Base.metadata.create_all(engine)
