# Convert list of names to uppercase
names = ["alice", "bob", "charlie", "diana"]

# Old Approach
upper_names_old = []
for name in names:
    upper_names_old.append(name.upper())
print(upper_names_old)

# List comprehension
upper_names = [name.upper() for name in names]
print(upper_names)
# Output: ['ALICE', 'BOB', 'CHARLIE', 'DIANA']

# Get lengths of each name
name_lengths = [len(name) for name in names]
print(name_lengths)
# Output: [5, 3, 7, 5]

# Add greeting to each name
greetings = [f"Hello, {name}!" for name in names]
print(greetings)
# Output: ['Hello, alice!', 'Hello, bob!', ...]