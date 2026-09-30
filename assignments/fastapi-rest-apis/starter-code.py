from fastapi import FastAPI

app = FastAPI(title="Student API")

students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student API"}


@app.get("/students")
def get_students():
    # Return the full list of students
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    # Find and return the student with the matching id
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "Student not found"}


@app.post("/students")
def create_student(student: dict):
    # Accept new student data and append it to the list
    students.append(student)
    return student
