# OLD WAY: Creating list of squares
squares_old = []
for num in range(1, 11):
    squares_old.append(num ** 2)

print("Old way:", squares_old)

# NEW WAY: List comprehension
squares_new = [num ** 2 for num in range(1, 11)] # i can do this in one line

print("New way:", squares_new)

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]