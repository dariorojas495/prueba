from pydantic import BaseModel, RootModel
from typing import List, Dict

class MedicalResultEntry(BaseModel):
    id: str
    data: List[str]
    deviceName: str

class MedicalResultCreate(RootModel):
    root: Dict[str, MedicalResultEntry]

class MedicalResultResponse(BaseModel):
    external_id: str
    device_id: int
    average_before: float
    average_after: float
    data_size: int
