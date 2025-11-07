import json

# List of students
students = [
    {"name": "Alice", "age": 17, "grade": "A"},
    {"name": "Bob", "age": 18, "grade": "B"},
    {"name": "Charlie", "age": 17, "grade": "A+"}
]

# Write to JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=5)  # Pretty-print with indentation5

print("Students JSON file created!")