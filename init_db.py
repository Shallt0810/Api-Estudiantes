from app.database.db_config import engine, Base, SessionLocal
from app.models.student import Student
from datetime import date

def setup_database():
    print("--- Proceso de Inicialización ---")
    
    # Crea las tablas
    Base.metadata.create_all(bind=engine)
    print("1. Tablas creadas en university.db")

    db = SessionLocal()
    try:
        # Check if empty
        if db.query(Student).count() == 0:
            print("2. Insertando 10 registros de prueba...")
            test_data = [
                Student(first_name="John", last_name="Doe", email="john.doe@university.edu", major="CS", semester=5, gpa=3.8, enrollment_date=date(2022, 8, 15)),
                Student(first_name="Jane", last_name="Smith", email="jane.s@university.edu", major="Biology", semester=3, gpa=3.9, enrollment_date=date(2023, 1, 10)),
                Student(first_name="Mike", last_name="Brown", email="mike.b@university.edu", major="Physics", semester=8, gpa=3.1, enrollment_date=date(2020, 9, 5)),
                Student(first_name="Emily", last_name="Davis", email="emily.d@university.edu", major="CS", semester=2, gpa=3.5, enrollment_date=date(2023, 8, 20)),
                Student(first_name="Chris", last_name="Wilson", email="chris.w@university.edu", major="Math", semester=4, gpa=2.8, enrollment_date=date(2022, 2, 14)),
                Student(first_name="Anna", last_name="Taylor", email="anna.t@university.edu", major="Chemistry", semester=6, gpa=4.0, enrollment_date=date(2021, 8, 12)),
                Student(first_name="David", last_name="Miller", email="david.m@university.edu", major="CS", semester=7, gpa=3.2, enrollment_date=date(2021, 1, 20)),
                Student(first_name="Sarah", last_name="White", email="sarah.w@university.edu", major="History", semester=1, gpa=3.7, enrollment_date=date(2024, 1, 5)),
                Student(first_name="Kevin", last_name="Jones", email="kevin.j@university.edu", major="Engineering", semester=9, gpa=2.5, enrollment_date=date(2020, 1, 15)),
                Student(first_name="Laura", last_name="Hall", email="laura.h@university.edu", major="Engineering", semester=10, gpa=3.6, enrollment_date=date(2019, 8, 30))
            ]
            db.add_all(test_data)
            db.commit()
            print("3. ¡Éxito! 10 estudiantes creados.")
        else:
            print("2. La base de datos ya tiene registros.")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    setup_database()
    