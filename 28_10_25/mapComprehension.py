# Create dictionary: number -> square
squares_dict = {num: num ** 2 for num in range(1, 6)}


# Old traditional way
squares_dict_old = {}
for num in range(1, 6):
    squares_dict_old[num] = num ** 2

print(f"Old approach {squares_dict_old}")

print(squares_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create dictionary: name -> length
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)
# Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Create dictionary: letter -> uppercase
letters = ['a', 'b', 'c']
upper_dict = {letter: letter.upper() for letter in letters}
print(upper_dict)
# Output: {'a': 'A', 'b': 'B', 'c': 'C'}