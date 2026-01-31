from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, DECIMAL
from sqlalchemy.sql import func
from app.database.db_config import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    major = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    gpa = Column(DECIMAL(3, 2))
    enrollment_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), server_default=func.now())
