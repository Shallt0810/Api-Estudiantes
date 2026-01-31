def validate_gpa(gpa: float):
    if gpa < 0.0 or gpa > 4.0:
        raise ValueError("GPA must be between 0.0 and 4.0")

def validate_semester(semester: int):
    if semester < 1 or semester > 12:
        raise ValueError("Semester must be between 1 and 12")
