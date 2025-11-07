import requests
import json

URL = "http://127.0.0.1:8000"

# HELPERS

def load_data(fileName: str):
    try:
        with open(fileName, "r") as f:
            return json.load(f)
    except Exception as e:
        return []
def save_data(fileName: str, data):
    with open(fileName, "w") as f:
        return json.dump(data, f, indent=2)

# GRADE WORK

def get_grades(fileName: str):
    req = requests.get(f"{URL}/grades")
    save_data(fileName, req.json())
    print(req.json())
def get_by_id(grade_id):
    res = requests.get(f"{URL}/grades/{grade_id}")
    print(res.json())
def add_grade(fileName: str):
    grade = load_data(fileName)[0]
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
def change_grade(fileName: str):
    grade = load_data(fileName)[0]
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

def get_all_classes():
    req = requests.get(f"{URL}/classes")
    print(req.json())
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
def delete_class(id: int):
    res = requests.delete(f"{URL}/grades/{id}")
    print(res.json())
def change_class(filename: str):
    data = load_data(filename)[0]
    new_class = {
        "code": data["code"],
        "students": data["students"],
        "year": data["year"],
        "classroom_teacher": data["classroom_teacher"]
    }
    res = requests.put(f"{URL}/grades", json=data)
    print(res.json())

if __name__ == "__main__":
    # get_all_classes()
    # add_class("default code", ["name1", "name2", "name3"], 404, "default teacher")
    # delete_class("default code")
    # change_class("default code", ["name1", "name2", "name3", "name404"], 404, "default teacher")

    #New
    # get_grades("forClient/allGrades.json")
    # add_grade("forClient/gradeToAdd.json")
    # delete_grade("forClient/gradeDeleted.json", 6)
    # change_grade("forClient/gradeToPut.json")

    #Old
    # get_grades()
    # add_grade("Misha", "ICT", 12, "2025.11.03", "Alexey")
    # delete_grade(4)
    # change_grade(1, "Misha", "ICT", 11, "2025.11.05", "Alexey")
