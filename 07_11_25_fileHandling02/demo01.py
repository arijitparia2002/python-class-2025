import json

with open("student.json", "r") as file:
    student = json.load(file) # This converts JSON data to Python dictionary

    print(f"Student Information: {student}")
    print(type(student))  # Should show <class 'dict'>
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
    print(f"Subjects: {', '.join(student['subjects'])}")

    