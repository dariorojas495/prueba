from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/hospital"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        yield db