import tkinter as tk
import requests

# def hi():
#     print("Hello world")
#
# bt1 = tk.Button(text="Hello world", command=hi)
# bt1.pack()

URL = "http://127.0.0.1:8000"

def get_grades():
    req = requests.get(f"{URL}/grades")
    print(req.json())
def get_by_id(grade_id):
    res = requests.get(f"{URL}/grades/{grade_id}")
    print(res.json())
def add_grade(name: str, subject: str, grade: int, date: str, teacher: str):
    data = {
        "name": name,
        "subject": subject,
        "grade": grade,
        "date": date,
        "teacher": teacher
    }
    res = requests.post(f"{URL}/grades", json=data)
    print(res.json())
def delete_grade(grade_id):
    res = requests.delete(f"{URL}/grades/{grade_id}")
    print(res.json())
def change_grade(grade_id: int, name: str, subject: str, grade: int, date: str, teacher: str):
    data = {
        "id": grade_id,
        "name": name,
        "subject": subject,
        "grade": grade,
        "date": date,
        "teacher": teacher
    }
    res = requests.put(f"{URL}/grades", json=data)
    print(res.json())

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Что-то на подобие postman")
    window.geometry("400x250")
    window.config(bg="#131417")

    labRunning = tk.Label(text="Running: ", bg="#131417", fg="#A9B7C6")
    labRunning.grid(row=1, column=1)

    labIsRunning = tk.Label(text="...", bg="#131417", fg="#A9B7C6")

    labIsRunning.grid(row=1, column=2)

    # lambda: get_grades() == get_grades

    bt1 = tk.Button(text="Get", command=lambda: get_grades(), bg="#B0B0B0")
    bt1.grid(row=2, column=1)

    bt2 = tk.Button(text="Add", command=get_grades, bg="#B0B0B0")
    bt2.grid(row=3, column=1)

    bt3 = tk.Button(text="Delete", command=get_grades, bg="#B0B0B0")
    bt3.grid(row=4, column=1)

    labId = tk.Label(text="Enter id:", bg="#131417", fg="#A9B7C6")
    labId.grid(row=4, column=2)

    tId = tk.Text(height=1, width=10, bg="#2B2B2B", fg="#A9B7C6")
    tId.grid(row=4, column=3)

    bt4 = tk.Button(text="Put", command=get_grades, bg="#B0B0B0")
    bt4.grid(row=5, column=1)
    pass
    # get_grades()
    # add_grade("Misha", "ICT", 12, "2025.11.03", "Alexey")
    # delete_grade(4)
    #change_grade(1, "Misha", "ICT", 11, "2025.11.05", "Alexey")
    window.mainloop()