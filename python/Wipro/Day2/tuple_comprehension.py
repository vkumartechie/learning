#python doesn't support direct tuple comprehension, but we can use generator expressions
#  to create tuples. Here's an example of how to create a tuple using a generator expression:
my_tuple = tuple(x for x in range(1,11))
print(my_tuple)  # prints (0, 1, 2, 3, 4)

#with condition
even_tuple = tuple(x for x in range(1,11) if x%2==0)
print(even_tuple)  # prints (2, 4, 6, 8, 10)

#with string example
string_tuple = tuple(char for char in "hello")
print(string_tuple)  # prints ('h', 'e', 'l', 'l', 'o')

