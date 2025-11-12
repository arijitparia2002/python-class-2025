import csv
import os

# File to store contacts
FILE_NAME = "contacts.csv"

# Ensure file exists with header
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\nAll Contacts:")
        for row in reader:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
    print()

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].lower() == search_name:
                print(f"\nFound: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                found = True
                break
    if not found:
        print("Contact not found.\n")

def delete_contact():
    name_to_delete = input("Enter name to delete: ").strip().lower()
    contacts = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0].lower() != name_to_delete:
                contacts.append(row)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(contacts)

    print(f"Contact '{name_to_delete}' deleted (if existed).\n")

def main():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
