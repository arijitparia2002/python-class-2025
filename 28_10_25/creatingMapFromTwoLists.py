# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

person = {keys[i]: values[i] for i in range(len(keys))}
print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Better way using zip
person2 = {k: v for k, v in zip(keys, values)}
print(person2)
# Same output

# Product prices
products = ["apple", "banana", "orange"]
prices = [1.50, 0.75, 2.00]
price_dict = {p: price for p, price in zip(products, prices)}
print(price_dict)

# Output: {'apple': 1.5, 'banana': 0.75, 'orange': 2.0}