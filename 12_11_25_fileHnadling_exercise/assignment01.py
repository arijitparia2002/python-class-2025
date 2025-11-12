import csv
import os

file = "tasks.csv"

# Load tasks
def load_tasks():
    tasks = []
    if os.path.exists(file):
        with open(file, "r") as f:
            for t, s in csv.reader(f):
                tasks.append([t, s])
    return tasks

# Save tasks
def save_tasks(tasks):
    with open(file, "w", newline="") as f:
        # write a header also
        #csv.writer(f).writerow(["Task", "Status"])
        csv.writer(f).writerows(tasks)

# Add task
def add_task(tasks):
    t = input("Enter new task: ")
    tasks.append([t, "Pending"])
    print("Task added!")

# View all
def view_tasks(tasks):
    for i, (t, s) in enumerate(tasks, 1):
        print(f"{i}. {t} - {s}")

# Mark complete
def complete_task(tasks):
    view_tasks(tasks)
    n = int(input("Task number to complete: "))
    tasks[n-1][1] = "Done"
    print("Task marked as done!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    n = int(input("Task number to delete: "))
    tasks.pop(n-1)
    print("Task deleted!")

# Main menu
tasks = load_tasks()
while True:
    print("\n1.Add  2.View  3.Complete  4.Delete  5.Save & Exit")
    c = input("Choose: ")

    if c == "1": add_task(tasks)
    elif c == "2": view_tasks(tasks)
    elif c == "3": complete_task(tasks)
    elif c == "4": delete_task(tasks)
    elif c == "5":
        save_tasks(tasks)
        print("Saved! Bye 👋")
        break
    else:
        print("Invalid choice!")