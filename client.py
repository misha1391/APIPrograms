import requests
import json

URL = "http://127.0.0.1:8000"

# HELPERS

def load_data(filename: str):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        return []
def save_data(filename: str, data):
    with open(filename, "w") as f:
        return json.dump(data, f, indent=2)

# GRADE WORK

def get_grades(filename: str):
    req = requests.get(f"{URL}/grades")
    save_data(filename, req.json())
    print(req.json())
def get_grade_by_id(grade_id: int):
    res = requests.get(f"{URL}/grades/{grade_id}")
    print(res.json())
def add_grade(filename: str):
    grade = load_data(filename)[0]
    data = {
        "name": grade["name"],
        "subject": grade["subject"],
        "grade": grade["grade"],
        "date": grade["date"],
        "teacher": grade["teacher"]
    }
    res = requests.post(f"{URL}/grades", json=data)
    print(res.json())
def delete_grade(filename:str, grade_id: int):
    res = requests.delete(f"{URL}/grades/{grade_id}")
    save_data(filename, res.json())
    print(res.json())
def change_grade(filename: str):
    grade = load_data(filename)[0]
    data = {
        "id": grade["id"],
        "name": grade["name"],
        "subject": grade["subject"],
        "grade": grade["grade"],
        "date": grade["date"],
        "teacher": grade["teacher"]
    }
    res = requests.put(f"{URL}/grades", json=data)
    print(res.json())

# CLASS WORK

def get_all_classes(filename: str):
    req = requests.get(f"{URL}/classes")
    save_data(filename, req.json())
    print(req.json())
def get_class_by_id(class_id: int):
    res = requests.get(f"{URL}/grades/{class_id}")
    print(res.json())
def add_class(filename: str):
    data = load_data(filename)[0]
    new_class = {
        "code": data["code"],
        "students": data["students"],
        "year": data["year"],
        "classroom_teacher": data["classroom_teacher"]
    }
    res = requests.post(f"{URL}/classes", json=data)
    print(res.json())
def delete_class(filename: str, id: int):
    res = requests.delete(f"{URL}/classes/{id}")
    save_data(filename, res.json())
    print(res.json())
def change_class(filename: str):
    data = load_data(filename)[0]
    new_class = {
        "id": data["id"],
        "code": data["code"],
        "students": data["students"],
        "year": data["year"],
        "classroom_teacher": data["classroom_teacher"]
    }
    res = requests.put(f"{URL}/classes", json=data)
    print(res.json())

if __name__ == "__main__":
    # get_all_classes("forClient/class/allClasses.json")
    # get_class_by_id(1)
    # add_class("forClient/class/addClass.json")
    # delete_class("forClient/class/deletedClass.json", 2)
    # change_class("forClient/class/putClass.json")

    #New
    # get_grades("forClient/grade/allGrades.json")
    # get_grade_by_id(5)
    # add_grade("forClient/grade/gradeToAdd.json")
    # delete_grade("forClient/grade/gradeDeleted.json", 6)
    # change_grade("forClient/grade/gradeToPut.json")

    #Old(Not working now)
    # get_grades()
    # add_grade("Misha", "ICT", 12, "2025.11.03", "Alexey")
    # delete_grade(4)
    # change_grade(1, "Misha", "ICT", 11, "2025.11.05", "Alexey")
