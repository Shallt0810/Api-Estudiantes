from fastapi import FastAPI
from app.database.db_config import Base, engine
from app.routes.student_routes import router as student_router

# Automatically create database tables on startup if they don't exist
# This uses the metadata from all models that inherit from Base
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI(
    title="Student Management API",
    description="REST API for managing university students",
    version="1.0.2"
)

# Register the students router with a global prefix
# All student-related endpoints will start with /api/students
app.include_router(student_router, prefix="/api/students", tags=["Students"])
