
with open("Grades.csv", "r") as file:
    for line in file:
        # print(line.strip())
        print(line.strip().split(","))


with open("Grades.csv", "a") as file:
    file.write("\nJohn, 85, 90, 78, 92")   
    file.write("\nArijit, 88, 76, 92, 85")


with open("Grades.csv", "r") as file:
    line1 = file.readline()
    headers = line1.split(",")
    for h in headers:
        print(h)