import json

# Define student data
student = [{
    "name": "Charlie",
    "age": 19,
    "grade": "13th",
    "subjects": ["Math", "Computer Science", "English"]
}]

# Write to JSON file
with open("student_output.json", "r+") as file:
    data = json.load(file)
    students_list = [data] 
    students_list.append(student[0])
    file.seek(0)  
    json.dump(students_list, file, indent=4)

print("JSON file updated!")