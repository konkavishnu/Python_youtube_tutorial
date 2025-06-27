def hello_world():
    print("Hello World !")


hello_world()


#  NOTE: to name a function we need to use only small letters , no CAPS is allowed and underscore should be used to have
#  space between words , no hyphens should be used. Also, 2 space lines should be there below a function.


def add(x, y):
    return x + y


print(add(1, 2))
print(add(3, 4))


def multiple_items(*args):  # --> will return tuple
    print(args)
    print(type(args))


multiple_items(1, 2, 3, 4)


def mult_named_items(**kwargs):  # --> keyword arguments (KWARGS) , can be used to return dictionary
    print(kwargs)
    print(type(kwargs))


mult_named_items(a=1, b=2, c=3)

# NOTE : In python all functions by default returns "None", we can do this by directly printing the function ,
#        try this code - print(greet("vishnu","vardhan")) and it will return none , unless we write return value
#        the function.   
# ---------------------------------------------------------------------------------------------------

def greet(first_name, last_name):
    print("welcome to the greet func "+first_name+" "+last_name)
    
greet("Vishnu","Vardhan")

def get_greeting(name):
    return f"Hi {name}"



message = get_greeting("Vishnu")
print(message)

#---------------------------------------------------------------------------------------------------

def increment(number, by):
    return number + by

result = increment(1,2)
print(increment(1,2))  # --> here we directly call the function instead of assigning it to variable

# we can also pass the arguments like below ,
print(increment(number=1,by=2))

#-----------------------------------------------------------------------------------------------------------------------------------------

# Default or optional parameters:
#--------------------------------

def default_para(number , by=1): # --> note that the default or optional parameters should be mentioned only after the normal parameters
    return number+by

print(default_para(2)) # --> here we did not pass the 2nd parameter as we defined it by a default value
print(default_para(2,5)) # --> here we gave a new value to the 2nd parameter and the new value will be considered

#------------------------------------------------------------------------------------------------------------------------------------------
# Passing data structures like tuple as parameter
#------------------------------------------------------

def multiply(*numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply(2,3,4,5))    

#--------------------------------------------------------------------------------------------------------------------------------------------
# Passing Dictionary as parameter
#---------------------------------

def save_user(**user):
    print(user)
    print(user["name"])
    
save_user(id=12, name="jhon", age=34)  #--> this will return a key value pair

#-------------------------------------------------------------------------------------------------------------------------------------

def fizz_buzz(input):
    if(input % 3 == 0):
        return"fizz"
    elif(input % 3 == 0 and input % 5 == 0):
        return "fizz_buzz"
    elif(input % 5 == 0):
        return "buzz"
    elif(input % 3 != 0 and input % 5 != 0):
        return input
        
print(fizz_buzz(15))