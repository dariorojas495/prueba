from fastapi import FastAPI
from routers import devices, medical_results

app = FastAPI(title="Medical Image Processing API")

# Incluir routers
app.include_router(devices.router, prefix="/devices", tags=["Devices"])
app.include_router(medical_results.router, prefix="/medical-results", tags=["Medical Results"])

@app.get("/")
def home():
    return {"message": "Medical Image Processing API is running!"}
