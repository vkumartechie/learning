# Lists in Python
# Ordered, mutable collections of items

# 1. Creating lists
print("=== Creating Lists ===")
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
list_of_lists = [[1, 2], [3, 4], [5, 6]]

print(f"Numbers: {numbers}")
print(f"Mixed List: {mixed_list}")

# 2. Accessing elements (indexing)
print("\n=== Indexing ===")
fruits = ["Apple", "Banana", "Cherry", "Date"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

# 3. List slicing
print("\n=== Slicing ===")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"numbers[2:5]: {numbers[2:5]}")
print(f"numbers[:3]: {numbers[:3]}")
print(f"numbers[5:]: {numbers[5:]}")
print(f"numbers[::2]: {numbers[::2]}")

# 4. Adding elements
print("\n=== Adding Elements ===")
colors = ["Red", "Blue"]
colors.append("Green")
print(f"After append: {colors}")
colors.extend(["Yellow", "Orange"])
print(f"After extend: {colors}")
colors.insert(1, "Purple")
print(f"After insert at index 1: {colors}")

# 5. Removing elements
print("\n=== Removing Elements ===")
items = [1, 2, 3, 4, 5]
items.remove(3)
print(f"After remove(3): {items}")
popped = items.pop()
print(f"Popped element: {popped}, List: {items}")
del items[0]
print(f"After del items[0]: {items}")

# 6. List methods
print("\n=== List Methods ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

numbers_sorted = sorted(numbers)
print(f"Sorted: {numbers_sorted}")

# 7. Iterating through lists
print("\n=== Iteration ===")
for fruit in ["Apple", "Banana", "Cherry"]:
    print(f"- {fruit}")

# 8. List comprehension
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")
