#tuple 
my_tuple=(1,2,3,4,5)
t2=(1,2,3,4,5, None)
t3=(1,) #single element tuple
print(my_tuple)  # prints the entire tuple
print(my_tuple[0])  # prints the first element
t4=tuple(1,2,3,4,5)
print(t4)  # prints the entire tuple


#indexing
print(my_tuple[1])  # prints the second element
print(my_tuple[-1])  # prints the last element

#slicing
print(my_tuple[1:4])  # prints elements from index 1 to 3
print(my_tuple[:3])  # prints the first three elements
print(my_tuple[2:])  # prints elements from index 2 to the end
print(my_tuple[:])  # prints the entire tuple
print(my_tuple[::2])  # prints every second element
print(my_tuple[1::2])  # prints every second element starting from index 1])
print(my_tuple[::-1])  # prints the tuple in reverse order 

#concatenation
t5=my_tuple+t2  # concatenates my_tuple and t2
print(t5)  # prints the concatenated tuple

#repetition
t6=my_tuple*2  # repeats my_tuple twice
print(t6)  # prints the repeated tuple

#membership
print(3 in my_tuple)  # prints True if 3 is in my_tuple, else False
print(6 in my_tuple)  # prints True if 6 is in my_tuple, else False

#adding and removing element is not possible in tuple as it is immutable

#finding the index of an element in a tuple
print(my_tuple.index(3))  # prints the index of the first occurrence of 3

#repeating the tuple
t=(1,2,3)
t7=t*3  # repeats the tuple t three times
print(t7)  # prints the repeated tuple

