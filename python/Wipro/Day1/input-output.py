age = input("Enter your age: ")
name=input("Enter your name: ")
print("my name is ",name, "and age is",age)  # This will print the age as a string
print(type(age))  # This will print <class 'str'> since input() returns a string
print(f"My name is {name} and age is {age}")  # Using f-string for formatted output
