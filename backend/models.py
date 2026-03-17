from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    messages = relationship("Message", back_populates="user")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    text = Column(String, nullable=False)
    is_from_user = Column(Boolean, default=True)
    topic_family = Column(Boolean, default=False)
    topic_peer = Column(Boolean, default=False)
    topic_career = Column(Boolean, default=False)
    topic_other = Column(Boolean, default=False)
    risk_level = Column(Integer, default=0)  # 0=typical,1=high,2=crisis
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="messages")

