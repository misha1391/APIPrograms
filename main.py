from fastapi import FastAPI
from typing import Dict, Any # Нужно для объявления внутри add_grade
import uvicorn
import json
# Нужно использовать uvicorn
app = FastAPI()

JSON_GRADE = "grades.json"
JSON_CLASSES = "classesList.json"

# HELPERS

def load_data(filename: str):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        return []
def save_data(filename: str, grades):
    with open(filename, "w") as f:
        return json.dump(grades, f, indent=2)
def generate_id(filename: str):
    grades = load_data(filename)
    if not grades:
        return 0
    #  Телеграмм лучше
    return max(grade["id"] for grade in grades) + 1

# GRADE WORK

@app.get("/grades") # Отправить клиенту
def get_grades():
    return load_data(JSON_GRADE)
@app.get("/grades/{grade_id}")
def get_grade_by_id(grade_id: int):
    grades = load_data(JSON_GRADE)
    for grade in grades:
        if grade["id"] == grade_id:
            return grade
    return {"ERROR": "Нет такой оценки"}
# в cmd - curl -X POST "Адрес"
@app.post("/grades") # Отправить от клиента
def add_grade(data: Dict[str, Any]):
    grades = load_data(JSON_GRADE)
    new_grade = {
        "id": generate_id(JSON_GRADE),
        "name": data["name"],
        "subject": data["subject"],
        "grade": data["grade"],
        "date": data["date"],
        "teacher": data["teacher"]
    }

    grades.append(new_grade)
    save_data(JSON_GRADE, grades)
    return {"Success": "Failure"}
@app.delete("/grades/{grade_id}")
def delete_grade(grade_id: int):
    grades = load_data(JSON_GRADE)
    for i, grade in enumerate(grades):
        if grade["id"] == grade_id:
            deleted_grade = grades.pop(i)
            save_data(JSON_GRADE, grades)
            return deleted_grade
    return {"ERROR": "Нет такой оценки"}
@app.put("/grades")
def change_grade(data: Dict[str, Any]):
    grades = load_data(JSON_GRADE)
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
            save_data(JSON_GRADE, grades)
            return {"Success": "Failure"}
    return {"ERROR": "Нет такой оценки"}

# CLASS WORK

@app.get("/classes")
def get_all_classes():
    return load_data(JSON_CLASSES)
@app.post("/classes")
def add_class(data: Dict[str, Any]):
    classes = load_data(JSON_CLASSES)
    new_class = {
        "id": generate_id(JSON_CLASSES),
        "code": data["code"],
        "students": data["code"],
        "year": data["code"],
        "classroom_teacher": data["code"]
    }

    classes.append(new_class)
    save_data(JSON_CLASSES, classes)
    return {"Success": "Failure"}
@app.delete("/classes/{class_id}")
def delete_class(class_id: int):
    classes = load_data(JSON_CLASSES)
    for i, clas in enumerate(classes):
        if clas["id"] == class_id:
            deleted_class = classes.pop(i)
            save_data(JSON_CLASSES, classes)
            return deleted_class
    return {"ERROR": "Нет такого класса"}
@app.put("/classes")
def change_class(data: Dict[str, Any]):
    classes = load_data(JSON_CLASSES)
    new_class = {
        "id": data["id"],
        "code": data["code"],
        "students": data["students"],
        "year": data["year"],
        "classroom_teacher": data["classroom_teacher"]
    }
    for i, clas in enumerate(classes):
        if clas["id"] == data["id"]:
            classes[i] = new_class
            save_data(JSON_CLASSES, classes)
            return {"Success": "Failure"}
    return {"ERROR": "Нет такого класса"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
