from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, DECIMAL
from sqlalchemy.sql import func
from app.database.db_config import Base

class Student(Base):
    """
    SQLAlchemy model representing the 'students' table in the database.
    This class defines the structure and constraints for student records.
    """
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True) # Primary key: Unique identifier for each student (Auto-incremented)
    
    # Personal details with character limits
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    email = Column(String(80), unique=True, nullable=False) # Email must be unique and cannot be null

    # Academic information
    major = Column(String(50), nullable=False)
    semester = Column(Integer, nullable=False)

    gpa = Column(DECIMAL(3, 2)) # GPA uses DECIMAL for precision (3 digits total, 2 after the decimal point)

    enrollment_date = Column(Date, nullable=False)# Enrollment and status

    is_active = Column(Boolean, default=True)# Soft delete flag: 1 (True) for active, 0 (False) for inactive

    # Audit timestamps: Track when a record was created and last modified
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), server_default=func.now())
