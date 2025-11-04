# import calculator

# addresult = calculator.add(10, 5)
# subresult = calculator.subtract(10, 5)
# mulresult = calculator.multiply(10, 5)
# divresult = calculator.divide(10, 5)

import calculator as calc # using alias


addresult = calc.add(10, 5)
subresult = calc.subtract(10, 5)
mulresult = calc.multiply(10, 5)
divresult = calc.divide(10, 5)


print(f"Addition Result: {addresult}")
print(f"Subtraction Result: {subresult}")
print(f"Multiplication Result: {mulresult}")
print(f"Division Result: {divresult}")

from calculator import add, subtract, multiply # when you want a specific function to be imported
from calculator import * # import everything from calculator module

addresult = add(10, 5)
subresult = subtract(10, 5)
mulresult = multiply(10, 5)
divresult = divide(10, 5)

print(f"Addition Result: {addresult}")
print(f"Subtraction Result: {subresult}")
print(f"Multiplication Result: {mulresult}")
print(f"Division Result: {divresult}")