import json

def load_contacts():
    """Load contacts"""
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    """Save contacts"""
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    """Add new contact"""
    contacts = load_contacts()
    new_contact = {
        "id": len(contacts) + 1,
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Added: {name}")

def view_contacts():
    """View all contacts"""
    contacts = load_contacts()
    if not contacts:
        print("No contacts!")
        return
    
    print("\nAll Contacts:")
    print("="*50)
    for contact in contacts:
        print(f"{contact['id']}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}\n")

# Usage
# add_contact("Alice", "123-456-7890", "alice@email.com")
# add_contact("Bob", "234-567-8901", "bob@email.com")
        
add_contact("Arijit", "345-678-9012", "arijit@mail.com")
view_contacts()