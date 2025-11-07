import json

student = {
    "name": "Charlie",
    "age": 17,
    "grade": "12th",
    "subjects": ["Biology", "Chemistry", "Physics"],
    "scores": {
        "biology": 90,
        "chemistry": 88,
        "physics": 92
    }
}

# Write with indentation
with open("student_formatted.json", "w") as file:
    json.dump(student, file, indent=4)

print("Formatted JSON created!")