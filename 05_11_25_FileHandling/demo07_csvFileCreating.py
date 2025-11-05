fruitsList = [
    ["Fruit", "Quantity", "Price"],
    ["Apple", 10, 0.5],
    ["Banana", 20, 0.2],
    ["Orange", 15, 0.3]
]

import csv
with open("Fruits.csv", "w", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerows(fruitsList)


# list of dictionaries
employeesList = [
    {"Name": "Alice", "Age": 30, "Department": "HR"},
    {"Name": "Bob", "Age": 25, "Department": "IT"},
    {"Name": "Charlie", "Age": 28, "Department": "Finance"}
]

import csv
with open("Employees.csv", "w", newline="\n") as file:
    fieldnames = ["Name", "Age", "Department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employeesList)