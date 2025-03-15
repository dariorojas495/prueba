from sqlalchemy import Column, Integer, String
from database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, unique=True, index=True)
