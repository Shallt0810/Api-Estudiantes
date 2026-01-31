from sqlalchemy.orm import Session
from app.models.student import Student

def get_all_students(db: Session, filters: dict):
    query = db.query(Student)

    if filters.get("major"):
        query = query.filter(Student.major == filters["major"])
    if filters.get("semester"):
        query = query.filter(Student.semester == filters["semester"])
    if filters.get("is_active") is not None:
        query = query.filter(Student.is_active == filters["is_active"])

    return query.all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()

def create_student(db: Session, data: dict):
    student = Student(**data)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def update_student(db: Session, student: Student, data: dict):
    for key, value in data.items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student

def soft_delete_student(db: Session, student: Student):
    student.is_active = False
    db.commit()
