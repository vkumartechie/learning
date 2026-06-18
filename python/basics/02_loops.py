# Loops in Python
# Used to execute a block of code multiple times

# 1. For Loop - iterates over a sequence
print("=== For Loop ===")
for i in range(5):
    print(f"Iteration {i}")

# For loop with list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# For loop with range and step
print("\n=== For Loop with Step ===")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 2. While Loop - executes while condition is true
print("\n=== While Loop ===")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# 3. Break statement - exits the loop
print("\n=== Break Statement ===")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print()

# 4. Continue statement - skips current iteration
print("\n=== Continue Statement ===")
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
print()

# 5. Nested loops
print("\n=== Nested Loops ===")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})", end=" ")
print()
