import csv, os

file = "grades.csv"

# Load data
def load_data():
    students = []
    if os.path.exists(file):
        with open(file, "r") as f:
            for row in csv.reader(f):
                name, *grades = row
                students.append([name] + list(map(float, grades)))
    return students

# Save data
def save_data(students):
    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(students)
    print("✅ Data saved to grades.csv!")

# Add student
def add_student(students):
    name = input("Student name: ")
    grades = input("Enter grades (comma separated): ").split(",")
    grades = [float(g) for g in grades]
    students.append([name] + grades)
    print("Student added!")

# View all students
def view_students(students):
    for s in students:
        avg = sum(s[1:]) / len(s[1:])
        print(f"{s[0]} → Grades: {s[1:]} | Avg: {avg:.2f}")

# Find top student
def top_student(students):
    top = max(students, key=lambda s: sum(s[1:]) / len(s[1:]))
    avg = sum(top[1:]) / len(top[1:])
    print(f"🏆 Top Student: {top[0]} (Avg: {avg:.2f})")

# Generate report
def report(students):
    print("\n--- Grade Report ---")
    view_students(students)
    top_student(students)

# Main program
students = load_data()
while True:
    print("\n1.Add  2.View  3.Top  4.Report  5.Save & Exit")
    c = input("Choose: ")

    if c == "1": add_student(students)
    elif c == "2": view_students(students)
    elif c == "3": top_student(students)
    elif c == "4": report(students)
    elif c == "5":
        save_data(students)
        print("Bye 👋")
        break
    else:
        print("Invalid choice!")