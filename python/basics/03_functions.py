# Functions in Python
# Reusable blocks of code that perform specific tasks

# 1. Simple function with no parameters
def greet():
    print("Hello, World!")

greet()

# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# 3. Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# 4. Function with multiple return values
def get_person_info():
    return "John", 30, "Engineer"

name, age, job = get_person_info()
print(f"Name: {name}, Age: {age}, Job: {job}")

# 5. Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")  # Uses default exponent=2

# 6. Function with variable-length arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# 7. Function with keyword arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Charlie", age=28, city="NYC")

# 8. Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
