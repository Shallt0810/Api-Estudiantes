import sys
import os

# Ensure the 'app' directory is in the Python path to avoid ModuleNotFoundError
# This allows running the script from any location within the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.db_config import engine, Base
from app.models.student import Student
from sqlalchemy.orm import sessionmaker
from datetime import date

def run_init():
    """
    Initializes the database by creating tables and populating them 
    with initial test data (seeding).
    """
    print("Starting database initialization...")
    
   # 1. Physical Table Creation
    # Uses SQLAlchemy metadata to generate tables based on defined models
    Base.metadata.create_all(bind=engine)
    print("Base creates succesfully")

    # 2. Database Seeding
    # Creates a new session to interact with the database
    Session = sessionmaker(bind=engine)
    db = Session()

    try:
        # Check if the database is empty to prevent duplicate entries
        if db.query(Student).count() == 0:
            print("Interting record for test...")

            # List of Student objects to be inserted as initial data
            test_students = [
                Student(first_name="John", last_name="Doe", email="john.doe@university.edu", 
                        major="Computer Science", semester=5, gpa=3.8, enrollment_date=date(2022, 8, 15)),
                Student(first_name="Jane", last_name="Smith", email="jane.smith@university.edu", 
                        major="Biology", semester=3, gpa=3.9, enrollment_date=date(2023, 1, 10)),
                Student(first_name="Samuel", last_name="Bonilla", email="sam0810@university.edu", 
                        major="Computer Science", semester=7, gpa=2, enrollment_date=date(2022, 8, 15)),
                Student(first_name="Liana", last_name="Agui", email="liabo@university.edu", 
                        major="Administration", semester=11, gpa=4, enrollment_date=date(2020, 2, 17)),
                Student(first_name="Richard", last_name="Monte", email="apari@university.edu", 
                        major="Medicine", semester=6, gpa=2.8, enrollment_date=date(2022, 2, 14)),
                Student(first_name="Jane", last_name="Smith", email="jane.s@university.edu", 
                        major="Biology", semester=3, gpa=3.9, enrollment_date=date(2023, 1, 10)),
                Student(first_name="Mike", last_name="Brown", email="mike.b@university.edu", 
                        major="Physics", semester=8, gpa=3.1, enrollment_date=date(2020, 9, 5)),
                Student(first_name="Emily", last_name="Davis", email="emily.d@university.edu", 
                        major="CS", semester=2, gpa=3.5, enrollment_date=date(2023, 8, 20)),
                Student(first_name="Chris", last_name="Wilson", email="chris.w@university.edu", 
                        major="Math", semester=4, gpa=2.8, enrollment_date=date(2022, 2, 14)),
                Student(first_name="Anna", last_name="Taylor", email="anna.t@university.edu", 
                        major="Chemistry", semester=6, gpa=4.0, enrollment_date=date(2021, 8, 12)),
            ]
            # Bulk insert all student records
            db.add_all(test_students)
            db.commit() # Save changes to university.db
            print("Records inserted successfully.")
        else:
            print("Database already contains data. Skipping seeding.")
    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback() # Undo changes if an error occurs
    finally:
        db.close() # Ensure the connection is always closed

if __name__ == "__main__":
    run_init()
