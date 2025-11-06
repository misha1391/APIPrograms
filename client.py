import tkinter as tk
import requests
import json

# def hi():
#     print("Hello world")
#
# bt1 = tk.Button(text="Hello world", command=hi)
# bt1.pack()

URL = "http://127.0.0.1:8000"

def load_data(fileName: str):
    try:
        with open(fileName, "r") as f:
            return json.load(f)
    except Exception as e:
        return []
def save_data(fileName: str, data):
    with open(fileName, "w") as f:
        return json.dump(data, f, indent=2)
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
def delete_grade(grade_id):
    res = requests.delete(f"{URL}/grades/{grade_id}")
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

def get_all_classes():
    req = requests.get(f"{URL}/classes")
    print(req.json())
def add_class(code: str, students: list[str], year: int, classroom_teacher: str):
    data = {
        "code": code,
        "students": students,
        "year": year,
        "classroom_teacher": classroom_teacher
    }
    res = requests.post(f"{URL}/classes", json=data)
    print(res.json())
def delete_class(code: str):
    res = requests.delete(f"{URL}/grades/{code}")
    print(res.json())
def change_class(code: str, students: list[str], year: int, classroom_teacher: str):
    data = {
        "code": code,
        "students": students,
        "year": year,
        "classroom_teacher": classroom_teacher
    }
    res = requests.put(f"{URL}/grades", json=data)
    print(res.json())

if __name__ == "__main__":
    # get_all_classes()
    # add_class("default code", ["name1", "name2", "name3"], 404, "default teacher")
    # delete_class("default code")
    # change_class("default code", ["name1", "name2", "name3", "name404"], 404, "default teacher")
    window = tk.Tk()
    window.title("Что-то на подобие postman")
    window.geometry("400x250")
    window.config(bg="#131417")

    labRunning = tk.Label(text="Running: ", bg="#131417", fg="#A9B7C6")
    labRunning.grid(row=1, column=1)

    labIsRunning = tk.Label(text="...", bg="#131417", fg="#A9B7C6")
    labIsRunning.grid(row=1, column=2)

    # lambda: get_grades() == get_grades
    bt1 = tk.Button(text="Get", command=lambda: get_grades("forClient/allGrades.json"), bg="#B0B0B0")
    bt1.grid(row=3, column=1)

    bt2 = tk.Button(text="Add", command=lambda: add_grade("forClient/gradeToAdd.json"), bg="#B0B0B0")
    bt2.grid(row=4, column=1)

    bt3 = tk.Button(text="Delete", command=lambda: delete_grade(tId.get(1.0)), bg="#B0B0B0")
    bt3.grid(row=5, column=1)

    labId = tk.Label(text="Enter id:", bg="#131417", fg="#A9B7C6")
    labId.grid(row=5, column=2)

    tId = tk.Text(height=1, width=10, bg="#2B2B2B", fg="#A9B7C6")
    tId.grid(row=5, column=3)

    bt4 = tk.Button(text="Put", command=lambda: change_grade("forClient/gradeToPut.json"), bg="#B0B0B0")
    bt4.grid(row=6, column=1)
    # get_grades()
    # add_grade("Misha", "ICT", 12, "2025.11.03", "Alexey")
    # delete_grade(4)
    # change_grade(1, "Misha", "ICT", 11, "2025.11.05", "Alexey")
    window.mainloop()