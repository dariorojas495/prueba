from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from database import Base

class MedicalResult(Base):
    __tablename__ = "medical_results"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    average_before = Column(Float)
    average_after = Column(Float)
    data_size = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
