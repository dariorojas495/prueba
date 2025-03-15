from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from database import get_db
from models.medical_result import MedicalResult
from models.device import Device
from schemas.medical_result import MedicalResultCreate, MedicalResultResponse
from utils.normalization import normalize_data, calculate_average
import logging

router = APIRouter()

# Configurar logs para errores
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@router.post("/")
async def create_medical_results(payload: MedicalResultCreate, db: AsyncSession = Depends(get_db)):
    responses = []
    
    for key, entry in payload.root.items():
        try:
            matrix = [[int(num) for num in row.split()] for row in entry.data]
            average_before = calculate_average(matrix)
            normalized_matrix = normalize_data(matrix)
            average_after = calculate_average(normalized_matrix)


            result = await db.execute(select(Device).where(Device.device_name == entry.deviceName))
            device = result.scalars().first()


            if not device:
                device = Device(device_name=entry.deviceName)
                db.add(device)
                await db.commit()
                await db.refresh(device)


            result_exists = await db.execute(select(MedicalResult).where(MedicalResult.external_id == entry.id))
            if result_exists.scalars().first():
                raise HTTPException(status_code=400, detail=f"Duplicate entry: external_id {entry.id} already exists.")


            new_result = MedicalResult(
                external_id=entry.id,
                device_id=device.id,
                average_before=average_before,
                average_after=average_after,
                data_size=len(matrix) * len(matrix[0]),
            )

            db.add(new_result)
            await db.commit()
            await db.refresh(new_result)
            responses.append(new_result)

        except ValueError:
            raise HTTPException(status_code=400, detail=f"Entry {key} contains invalid data (non-numeric values)")
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Database error: {str(e)}")
            raise HTTPException(status_code=500, detail="Database error occurred")
        except Exception as e:
            await db.rollback()
            logger.error(f"Unexpected error: {str(e)}")
            raise HTTPException(status_code=500, detail="Unexpected error occurred")

    return responses



@router.get("/", response_model=list[MedicalResultResponse])
async def get_medical_results(
    created_date: str = Query(None),
    updated_date: str = Query(None),
    avg_before_min: float = Query(None),
    avg_before_max: float = Query(None),
    avg_after_min: float = Query(None),
    avg_after_max: float = Query(None),
    db: AsyncSession = Depends(get_db)
):
    try:
        query = select(MedicalResult)
        if created_date:
            query = query.where(MedicalResult.created_at >= created_date)
        if updated_date:
            query = query.where(MedicalResult.updated_at >= updated_date)
        if avg_before_min is not None:
            query = query.where(MedicalResult.average_before >= avg_before_min)
        if avg_before_max is not None:
            query = query.where(MedicalResult.average_before <= avg_before_max)
        if avg_after_min is not None:
            query = query.where(MedicalResult.average_after >= avg_after_min)
        if avg_after_max is not None:
            query = query.where(MedicalResult.average_after <= avg_after_max)

        result = await db.execute(query)
        return result.scalars().all()
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Unexpected error occurred")

@router.get("/{result_id}", response_model=MedicalResultResponse)
async def get_medical_result(result_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(MedicalResult).where(MedicalResult.id == result_id))
        medical_result = result.scalars().first()
        if not medical_result:
            raise HTTPException(status_code=404, detail="Medical result not found")
        return medical_result
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")

@router.put("/{result_id}", response_model=MedicalResultResponse)
async def update_medical_result(result_id: int, payload: MedicalResultCreate, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(MedicalResult).where(MedicalResult.id == result_id))
        medical_result = result.scalars().first()
        if not medical_result:
            raise HTTPException(status_code=404, detail="Medical result not found")

        # Validar si device_id existe
        device_result = await db.execute(select(Device).where(Device.id == payload.device_id))
        device = device_result.scalars().first()
        if not device:
            raise HTTPException(status_code=400, detail="Invalid device_id")

        try:
            matrix = [[int(num) for num in row.split()] for row in payload.data]
        except ValueError:
            raise HTTPException(status_code=400, detail="Data contains non-numeric values")

        medical_result.average_before = calculate_average(matrix)
        medical_result.average_after = calculate_average(normalize_data(matrix))
        medical_result.data_size = len(matrix) * len(matrix[0])
        medical_result.device_id = payload.device_id

        await db.commit()
        return medical_result
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")

@router.delete("/{result_id}")
async def delete_medical_result(result_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(MedicalResult).where(MedicalResult.id == result_id))
        medical_result = result.scalars().first()
        if not medical_result:
            raise HTTPException(status_code=404, detail="Medical result not found")

        await db.delete(medical_result)
        await db.commit()
        return {"message": "Medical result deleted successfully"}
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")
