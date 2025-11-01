contacts = [
    {"name": "Alice Johnson", "phone": "123-456-7890", "email": "alice@gmail.com", "city": "New York"},
    {"name": "Bob Smith", "phone": "234-567-8901", "email": "bob@yahoo.com", "city": "Los Angeles"},
    {"name": "Charlie Brown", "phone": "345-678-9012", "email": "charlie@gmail.com", "city": "Chicago"},
    {"name": "Diana Prince", "phone": "456-789-0123", "email": "diana@outlook.com", "city": "New York"},
    {"name": "Eve Wilson", "phone": "567-890-1234", "email": "eve@gmail.com", "city": "Boston"}
]


# Part A: Email Extraction
print("\n--- Part A: Email Extraction ---")
all_emails = [contact["email"] for contact in contacts]
print("All emails:", all_emails)


# CREATE NAME AND EMAILS DICTIONARY
name_email_dict = {contact["name"]: contact["email"] for contact in contacts}
print("Name and Email Dictionary:", name_email_dict)


# Part B: Phone Book
print("\n--- Part B: Phone Book ---")
phone_book = {contact["name"]: contact["phone"] for contact in contacts}
print("Phone Book:", phone_book)


# Part C: Search Function
print("\n--- Part C: Search Function ---")
def search_contact(name):
    """Search for contact by name (case-insensitive)"""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

search_name = "alice johnson"
result = search_contact(search_name)
print(f"Search result for '{search_name}':", result)


# Part D: Domain Analysis
print("\n--- Part D: Domain Analysis ---")
for contact in contacts:
    email = contact["email"]
    domain = email.split("@")[1]
    print(domain)
    contact["domain"] = domain

domain_count = {}
for contact in contacts:
    domain = contact["domain"]
    domain_count[domain] = domain_count.get(domain, 0) + 1

print("Domain distribution:")
for domain, count in sorted(domain_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{domain}: {count} contact(s)")  


# Part E: City Grouping
print("\n--- Part E: City Grouping ---")
city_groups = {}

for contact in contacts:
    city = contact["city"]
    if city not in city_groups:
        city_groups[city] = []
    city_groups[city].append(contact["name"])

print("Contacts grouped by city:")
for city, names in city_groups.items():
    print(f"{city}: {names}")
