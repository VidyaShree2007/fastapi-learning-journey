from fastapi import FastAPI

app = FastAPI()

# Home
@app.get("/")
def home():
    return {"message": "Student API is running"}


# 1. Path parameter
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }


# 2. Query parameters
@app.get("/students")
def search_student(name: str, age: int):
    return {
        "name": name,
        "age": age
    }


# 3. Path + Query parameter
@app.get("/students/{student_id}/course")
def get_course(student_id: int, course: str):
    return {
        "student_id": student_id,
        "course": course
    }