import csv

with open("Grades.csv", "r") as file:
    csvFileToDict = csv.DictReader(file)

    # printing the data of csv file line by line
    for line in csvFileToDict:
        # print(line['Name'])
        print(f"{line.get('Name')} has scored {line.get('Math')} in Maths")