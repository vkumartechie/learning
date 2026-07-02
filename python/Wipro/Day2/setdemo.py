s={1,2,3,4,5}
print(s)  # prints the entire set

#indexing is not supported in sets as they are unordered collections

#you can iterate over a set
for item in s:
    print(item)
    
#you can also use set comprehensions
squared_set = {x**2 for x in s}
print(squared_set)  # prints the set of squared values

#slicing
#slicing is not supported in sets as they are unordered collections

#membership
print(3 in s)  # prints True if 3 is in the set, else False
print(6 in s)  # prints True if 6 is in the set, else False
print(2 not in s)  # prints True if 2 is not in the set, else False

#adding elements to a set
s.add(6)  # adds 6 to the set
print(s)  # prints the updated set

#removing elements from a set
s.remove(3)  # removes 3 from the set
print(s)  # prints the updated set

s.discard(4)  # removes 4 from the set, does not raise an error if 4 is not present
print(s)  # prints the updated set

s.pop()  # removes and returns an arbitrary element from the set
print(s)  # prints the updated set

s.clear()  # removes all elements from the set
print(s)  # prints the empty set

s1={}
print(type(s1))  # prints <class 'dict'>, because {} creates an empty dictionary

s2=set()
print(type(s2))  # prints <class 'set'>, because set() creates an empty set

#finding the length of a set
print(len(s2))  # prints 0, as s2 is empty
