import csv
import json

def csv_to_json(csv_filename, json_filename):
    """Convert CSV to JSON"""
    data = []
    
    # Read CSV
    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    # Write JSON
    with open(json_filename, "a") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Converted {csv_filename} to {json_filename}")

# Test
# with open("students.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "Grade"])
#     writer.writerow(["Alice", "17", "A"])
#     writer.writerow(["Bob", "18", "B"])

csv_to_json("students.csv", "students_from_csv.json")