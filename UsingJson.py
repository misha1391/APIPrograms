from fastapi import FastAPI
from typing import Dict, Any # Нужно для объявления внутри add_grade
import uvicorn
import json
# Нужно использовать uvicorn
app = FastAPI()

JSON_FILE = "grades.json"

def load_data():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        return []

def save_data(grades):
    with open(JSON_FILE, "w") as f:
        return json.dump(grades, f, indent=2)

def generate_id():
    grades = load_data()
    if not grades:
        return 0
    #  Телеграмм лучше
    return max(grade["id"] for grade in grades) + 1

@app.get("/grades") # Отправить клиенту
def get_grades():
    return load_data()

# в cmd - curl -X POST "Адрес"
@app.post("/grades") # Отправить от клиента
def add_grade(data: Dict[str, Any]):
    grades = load_data()
    new_grade = {
        "id": generate_id(),
        "name": data["name"],
        "subject": data["subject"],
        "grade": data["grade"],
        "date": data["date"],
        "teacher": data["teacher"]
    }

    grades.append(new_grade)
    save_data(grades)
    return {"Success": "Failure"}

@app.delete("/grades/{grade_id}")
def delete_grade(grade_id: int):
    grades = load_data()
    for i, grade in enumerate(grades):
        if grade["id"] == grade_id:
            deleted_grade = grades.pop(i)
            save_data(grades)
            return deleted_grade
    return {"ERROR": "Нет такой оценки"}

@app.put("/grades")
def change_grade(data: Dict[str, Any]):
    grades = load_data()
    new_grade = {
        "id": data["id"],
        "name": data["name"],
        "subject": data["subject"],
        "grade": data["grade"],
        "date": data["date"],
        "teacher": data["teacher"]
    }
    for i, grade in enumerate(grades):
        if grade["id"] == data["id"]:
            grades[i] = new_grade
            save_data(grades)
            return {"Success": "Failure"}
    return {"ERROR": "Нет такой оценки"}

@app.get("/grades/{grade_id}")
def get_grade_by_id(grade_id: int):
    grades = load_data()
    for grade in grades:
        if grade["id"] == grade_id:
            return grade
    return {"ERROR": "Нет такой оценки"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
