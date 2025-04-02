bill = 1500
discount = 100
if bill > 2000:
    print("Bill is greater than 1000")
    bill = bill - discount

print("Final bill is", bill)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"i like {fruit}")


name = "Dadius"
for char in name:
    print(char)


for number in range(1, 6):
    print(f"Number: {number}")




for number in range(1, 10):
    if number == 5:
        print("Breaking the loop at 5")
        break
    elif number % 2 == 0:
        print(f"Skipping {number} because it is even")
        continue
    print(f"Processing number: {number}")

    #nested loops
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"outer loop: {i}, inner loop: {j}")

squares = []
for x in range(5):
    squares.append(x**2)
squares = [x**2 for x in range(5)]
print(squares)

matrix = [[i * j for j in range(1,4)] for i in range (1,4)] 
print(matrix)

names = ["Alice", "Bob", "Charlie"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

numbers = [10, 15, 20, 25, 30]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

result = []
for x in range(10):
    for y in range(5):
        result.append(x * y)
        print(result)
#positional arguments
def add(a, b):
    return a + b
print(add(3, 5))

#keyword arguments
def introduce(name, age):
    return f"My name is {name} and i am {age} years old"
print(introduce(name="Dadius", age = 24))

#default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
print(greet("Dadius"))

#lambda function for adding two numbers
add = lambda x, y: x + y
print(add(5, 10))

#using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#recursive functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#using filter with lamda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#using reduce with lambda
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

#large power
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
print(large_power(2, 13))

def divisable_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False
print(divisable_by_ten(203))

def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price
if discount >= 0.2:
    print("applying discount")
else:
    print("No discount applied")

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
original_price = float(input("Enter the original price:"))
discount = float(input("Enter the discount percentage:"))
final_price = calculate_discount(original_price, discount)
print(f"The final price after discount is: {final_price}")
