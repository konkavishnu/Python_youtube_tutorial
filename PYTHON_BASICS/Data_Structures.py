#                     LIST TYPE [ ]
#                    -----------

users = ["Vishnu", 34]
print(users)
print("Vishnu" in users)  # --> to check if "vishnu" is true or false in the list
print(users[0])   # --> this will return the 1st item on the list
print(users[-2])  # --> this will return the 2nd item from the end of the list
print(users.index("Vishnu"))
print(users[0:1])
print(users[:2])
print(users[0:])
print(len(users))

numbers = list(range(20))
print(numbers[::2])   # --> this will return the list with gap of 2
print(numbers[::-1])  # --> this will return the list in reverse order

users.append("Vishnu 2")  # --> append is used to add elements at the end of the list only
users += ["Vishnu"]  # --> shortcut to append an element to the existing list ,
# Note: '[]' is important else it will add each char of the string as elements to the list
print(users)

users.extend(["Soniya", 34])  # --> this will also extend or add elements to the list
print(users)

data = [34, 45, 67]
users.extend(data)  # --> this is will append the elements of another list to the existing list
print(users)

users.insert(0, 'bob')  # --> insert is to add elements into the list anywhere
print(users)

users[2:2] = ['Eddie']  # --> to add / insert the element to a particular index , here it inserted at index=2
print(users)

users[1:3] = ['New']  # --> to add /insert the element to a particular index , here it inserted at index=1
print(users)

users[1:3] = ['replaced 1', 'replaced 2']  # --> we can also replace the values in a list
print(users)

users.remove('bob')
print(users)
print(users.pop())  # --> This will remove only the last element & as well as returns the value
print(users)
del users[0]  # --> This will delete the element anywhere in the list, we can also delete the entire list by "del <name of the list>"
print(users)

data.clear()  # --> this will clear the element from the list

newList = [3, 2, 1, 4, 5]
newList.sort()  # --> sorts the list , note - we can sort only with same data type in the list
print(newList)

newList1 = [3, 2, 1, 4, 5]
newList1.reverse()  # --> this function will not sort the list in reverse order . It just flips the list
print(newList1)

newList2 = [3, 2, 1, 45, 55]
newList2.sort(reverse=True)  # --> this will sort the list in descending order.
print(newList2)

StringList = ["a", "B", "c", "D", "e", "f"]
StringList.sort(key=str.lower)  # -->  if we need to sort on any particular 'type' within the data type
print(StringList)
# NOTE : here we can pass our customized function in the 'key' to tell python to sort according to the function

# Global sort
newList3 = [3, 2, 13, 43, 53]
print(sorted(newList3, reverse=True))

# Copy List
newCopy = newList3.copy()
newCopy1 = list(newList3)
newCopy2 = newList3[:]
print(newCopy)
newCopy1.sort()
print(newCopy1)
print(newCopy2)

print(type(newList3))

# Creating new list shortcut

myList = list([1, 2, 3, 4, 5])

# creating list with for loop,

numbers = list(range(20))

# Unpacking Lists
#----------------
# Unpacking is a process of removing the data from a data structure .

num =[1,2,3,4,5,6]
first , second , *other = num  #--> here other will make a separate list of other items in the list 
print(first)
print(second)
print(other)

unpack = [*range(5), *"Hello"] # --> here we are unpacking list as well as strings

# ENUMERATE keyword 

for x in enumerate(num): # --> the enumerate will create a tuples for the elements of the list with thier index
    print(num)

#                           2D Lists []
#                           -----------

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7]
]
print(matrix[0][3])  # --> here [0] is the 1st row list and [3] is the 3rd element of the list

for row in matrix:  # --> here 'row' is the memory to store each rows of the 2D list
    for item in row:  # --> here 'item' is the memory to store each element inside each rows of the matrix
        print(item)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#                                    TUPLES ( )
#                                   --------
# NOTE : Tuples are same like Lists but the order and the data inside a tuple cannot be changed.

myTuple = tuple([1, 2, "Vishnu", 4, 5])
myTuple1 = (1, 2, 3, 4, 5)  # --> note that tuples are indicated with '( )' & lists are indicated with '[ ]'
print(type(myTuple1))

# Since tuples are immutable we need to copy it to a list and then manipulate it
CopyList = list(myTuple1)
CopyList.append("added")
CopyTuple = tuple(CopyList)
print(CopyTuple)

# Unpacking the tuple
(one, two, *hey) = myTuple1  # --> In this way we can assign names for our elements inside the tuple
print(one)  # --> this will print 1 from myTuple1
print(two)
print(*hey)  # when we indicate '*' it will pack all the remaining elements to it .

myTuple.count(2)  # --> gives the number of occurrences of the element 2 in the tuple


#  NOTE : There are many other functions with tuple which can be accessed with dot operator.


#---------------------------------------MAP , FILTER FUNCTION------------------------------------------------------------------------

items = [
    ("product 1",10),
    ("product 2", 9),
    ("product 3", 12)
]

x = list(map(lambda item:item[1], items))  # here map (lambda <variable to store the 1st tuple> : <the elemenrt in the nth index of the tuple> , <name of the list>)
print(x)

filtered = list(filter(lambda item:item[1] >= 10 , item))  # same as above with condition since it is filter
print(filtered)

# ZIP function: used to pack all iterables or data structures into one
#--------------

list1 = [1,2,3,4,5]
list2 = [78,98,90,45]

print(list(zip("abc",list1,list2))) 

#--------------------------------------------QUEUE------------------------------------------------------------------------

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # --> this will remove the element from the left

print(queue)

# Swapping 2 variables :
#-----------------------
x= 10
y=12

z=x
x=y
y=x

# we can also define like below,
x,y = y,x 
x,y = (11,23)

print("x", x)
print("y", y)

#---------------------------------------------------------------------------------------------------------------------------
#                                 ARRAYS
#                                 ------

from array import array

numbers = array("i",[1,2,3,4]) # --> here "i" is the typecode of int , we need to mention what data type we are going to store.
numbers[0] = 34
numbers.append(29)
# NOTE : Other functions of arrays are same as list
#        We can get the type codes from the internet.
#----------------------------------------------------------------------------------------------------------------------------




 
