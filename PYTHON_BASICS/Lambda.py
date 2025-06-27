squared = lambda num: num * num

print(squared(2))

addTwo = lambda num: num + 2  # --> The value of "num" is taken by the paramenter passed while calling the main
# function , like addTwo here

print(addTwo(2))

summing = lambda a,b: a+b
print(summing(1,2))

# We can also write like ,

def summing(a,b) : return a+b


####################################################################

def func_Builder(x):
    return lambda num : num + x

add_ten = func_Builder(10)
add_twenty = func_Builder(20)

print("Add 10 : ", add_ten(7))
print("Add 20: ", add_twenty(7))

########################################################################

# HIGHER ORDER FUNCTION
# -----------------------

lambda num : num * num

numbers = [3,7,12,18,20,21]

# MAP :
# ------

squared_nums = map(lambda num: num * num, numbers)
# map (<lambda condition to apply on each element> , <the collection on which the action should be performed>)

print(list(squared_nums))

# FILTER :
# ---------

odd_nums = filter(lambda num : num % 2 !=0 , numbers)
# filter(<lambda condition for filtering the elements> , <the collection on which the action should be performed>)
print(list(odd_nums))

