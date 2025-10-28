# Multiply all numbers by 2
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print("Doubled:", doubled)
# Output: [2, 4, 6, 8, 10]


# Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
# old approach converted to fahrenheit

fahrenheit_old = []
for temp in celsius:
    fahrenheit_old.append((temp * 9/5) + 32)
print("Fahrenheit (old):", fahrenheit_old)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]



# New Approach using list comprehension
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit:", fahrenheit)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# Calculate area of squares with different sides
sides = [2, 3, 4, 5]
areas = [side ** 2 for side in sides]
print("Areas:", areas)
# Output: [4, 9, 16, 25]