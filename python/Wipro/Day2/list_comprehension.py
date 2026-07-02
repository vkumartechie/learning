#[Expression for item in iterable if condition]
#list comprehension is a conscise way to create lists
squares=[x**2 for x in range(1,10)]
print(squares)

#list comprehension with condition

even_squares=[x**2 for x in range(1,10) if x%2==0]
print(even_squares) 
#with if else
result=[x**2 if x%2==0 else x**3 for x in range(1,10)]
print(result)

#nested list comprehension
matrix=[[i for j in range(3)] for i in range(3)]
print(matrix)
