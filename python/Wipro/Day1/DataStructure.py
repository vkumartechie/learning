#list(ordered, mutable, allow duplicate)
list1=[1,2,3,4,5, None]
print('list1-',list1)
#mutable can be modified after creation
list1[0]=10
print('list1 after modification-',list1)

#list can contain duplicate values
list2=[1,2,2,3,4,4,5]
print('list2-',list2)

#list can contain different data types
list3=[1,"hello",3.4,True]
print('list3-',list3)

#Set(unordered, mutable, no duplicate)
set1={1,2,3,4,5}
print('set1-',set1)

#mutable can be modified after creation
set1.add(6)
print('set1 after adding 6-',set1)

#Set cannot contain duplicate values
set2={1,2,2,3,4,4,5, None, None}
print('set :',set2)

#tuple(ordered, immutable, allow duplicate)
tuple1=(1,2,None,3,4,5, None)
print('tuple1-',tuple1)

#tuple cannot be modified after creation
#tuple1[0]=10  # This will raise an error

#dictionary(unordered, mutable, no duplicate keys)
dict1={"name":"vikash","age":21,"college":"wipro"}
print(dict1)

#dictionary can be modified after creation
dict1["age"]=22
print(dict1)

#dictionary cannot have duplicate keys
dict2={"name":"vikash","name":"john","age":21}
print(dict2)

#when can we use this
#list - shopping list, to do list, student marks
#set - unique values, removing duplicates from a list
#tuple - fixed dates, coordinates, RGB values, days of the week
#dictionary - student records, employee records, product details

