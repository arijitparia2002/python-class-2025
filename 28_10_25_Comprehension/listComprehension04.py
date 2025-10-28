# Filtering example with list comprehension


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Get only even numbers
evens = [num * 2 for num in numbers if num % 2 == 0]
print("Even numbers:", evens)
# Output: [2, 4, 6, 8, 10]

# Get only odd numbers
odds = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odds)
# Output: [1, 3, 5, 7, 9]

# Get numbers greater than 5
greater_than_5 = [num for num in numbers if num > 5]
print("Greater than 5:", greater_than_5)
# Output: [6, 7, 8, 9, 10]