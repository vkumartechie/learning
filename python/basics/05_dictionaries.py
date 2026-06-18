# Dictionaries in Python
# Unordered, mutable collections of key-value pairs

# 1. Creating dictionaries
print("=== Creating Dictionaries ===")
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
student = dict(name="Bob", age=20, grade="A")

print(f"Person: {person}")
print(f"Student: {student}")

# 2. Accessing values
print("\n=== Accessing Values ===")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country (with default): {person.get('country', 'USA')}")

# 3. Adding and modifying items
print("\n=== Adding/Modifying Items ===")
person["age"] = 31
print(f"After age update: {person}")
person["country"] = "USA"
print(f"After adding country: {person}")

# 4. Removing items
print("\n=== Removing Items ===")
info = {"a": 1, "b": 2, "c": 3, "d": 4}
del info["b"]
print(f"After del info['b']: {info}")
removed_value = info.pop("c")
print(f"Popped value: {removed_value}, Dict: {info}")

# 5. Dictionary methods
print("\n=== Dictionary Methods ===")
car = {"brand": "Toyota", "model": "Camry", "year": 2022}
print(f"Keys: {car.keys()}")
print(f"Values: {car.values()}")
print(f"Items: {car.items()}")
print(f"Length: {len(car)}")

# 6. Iterating through dictionaries
print("\n=== Iteration ===")
for key, value in car.items():
    print(f"{key}: {value}")

# 7. Checking if key exists
print("\n=== Key Existence ===")
print(f"'brand' in car: {'brand' in car}")
print(f"'color' in car: {'color' in car}")

# 8. Merging dictionaries
print("\n=== Merging Dictionaries ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# 9. Nested dictionaries
print("\n=== Nested Dictionaries ===")
company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "John", "role": "Developer"},
        "emp2": {"name": "Jane", "role": "Manager"}
    }
}
print(f"Company: {company['name']}")
print(f"Employee 1 name: {company['employees']['emp1']['name']}")

# 10. Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares}")
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares dict: {even_squares}")
