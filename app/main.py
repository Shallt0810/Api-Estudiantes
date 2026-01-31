from fastapi import FastAPI
from app.database.db_config import Base, engine
from app.routes.student_routes import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="REST API for managing university students",
    version="1.0.0"
)

app.include_router(student_router, prefix="/api/students", tags=["Students"])
