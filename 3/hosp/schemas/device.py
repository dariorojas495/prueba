from pydantic import BaseModel

class DeviceCreate(BaseModel):
    device_name: str

class DeviceResponse(DeviceCreate):
    id: int

    class Config:
        from_attributes = True
