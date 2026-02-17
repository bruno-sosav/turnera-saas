from sqlalchemy import Column, Integer, String, DateTime
from app.database.connection import Base

class Turn(Base):
    __tablename__ = "turns"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    service = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
