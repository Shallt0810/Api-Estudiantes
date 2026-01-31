from fastapi import APIRouter, Depends, HTTPException, status, Query
import sqlite3
from sqlalchemy.orm import Session
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from datetime import date

from app.database.db_config import SessionLocal
from app.controllers import student_controller

router = APIRouter()
DATABASE = "database.db"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- Schemas --------

class StudentBase(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: EmailStr
    major: str
    semester: int = Field(..., ge=1, le=12)
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    enrollment_date: date
    is_active: Optional[bool]

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    major: str
    semester: int = Field(..., ge=1, le=12)
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    enrollment_date: date

class StudentUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    major: Optional[str]
    semester: Optional[int] = Field(None, ge=1, le=12)
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    enrollment_date: Optional[date]
    is_active: Optional[bool]

# -------- Endpoints --------

@router.get("/", response_model=List[StudentBase])
def list_students(
    major: Optional[str] = None,
    semester: Optional[int] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    filters = {"major": major, "semester": semester, "is_active": is_active}
    return student_controller.get_all_students(db, filters)

@router.get("/students per page/")
def get_students_page(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=50)
):
    offset = (page - 1) * size

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE is_active = 1"
    )
    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT * FROM students
        WHERE is_active = 1
        LIMIT ? OFFSET ?
        """,
        (size, offset)
    )

    students = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return {
        "page": page,
        "size": size,
        "total_records": total,
        "total_pages": (total + size - 1) // size,
        "data": students
    }

@router.get("/{student_id}")
def get_student_per_id(student_id: int, db: Session = Depends(get_db)):
    student = student_controller.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if student_controller.get_student_by_email(db, student.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    return student_controller.create_student(db, student.dict())

@router.put("/{student_id}")
def update_student_full(student_id: int, student: StudentBase, db: Session = Depends(get_db)):
    existing = student_controller.get_student_by_id(db, student_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_controller.update_student(db, existing, student.dict())

@router.patch("/{student_id}")
def update_student_partial(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    existing = student_controller.get_student_by_id(db, student_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_controller.update_student(db, existing, student.dict(exclude_unset=True))

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = student_controller.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student_controller.soft_delete_student(db, student)
    return {"message": "Student deactivated successfully"}
