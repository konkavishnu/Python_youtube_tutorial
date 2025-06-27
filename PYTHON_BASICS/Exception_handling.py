try:
    age = int(input("Age: "))
except ValueError as e:
    print("Please enter the correct age")
    print(e)
else:
    print("No exceptions were thrown")
    
    
try:
    age = int(input("Age: "))
    Xfactor = 10 / age
except ValueError as e:
    print("Please enter the correct age")
    print(e)
except ZeroDivisionError :
    print("age cannot be 0")
else:
    print("No exceptions were thrown")
    

# NOTE : In the below code we have multiple "ZerodivisionError"
#        But python will not throw any error because the code 
#        propogation will be from try -> except or else. So , if there 
#        are multiple exceptions of the same type it will throw the exception which came first.

try:
    age = int(input("Age: "))
    Xfactor = 10 / age
except (ValueError,ZeroDivisionError):
    print("Please enter the correct age")
except ZeroDivisionError :
    print("age cannot be 0")
else:
    print("No exceptions were thrown")
    
# Finally :
#---------- 
try:
    file = open("test.py")
    age = int(input("Age: "))
    Xfactor = 10 / age
except (ValueError,ZeroDivisionError):
    print("Please enter the correct age")
except ZeroDivisionError :
    print("age cannot be 0")
else:
    print("No exceptions were thrown")
finally: #(same like java finally)
    file.close()
    
# With Statement:
#----------------

# WITH statement is used when working with files , we can wirte the operstions in the file 
# with an alias name . Also when using WITH statement the file is automatically closed 

try:
    with open("test.py") as file:
        print("file openned")
    age = int(input("Age: "))
    Xfactor = 10 / age
except (ValueError,ZeroDivisionError):
    print("Please enter the correct age")
except ZeroDivisionError :
    print("age cannot be 0")
else:
    print("No exceptions were thrown")
finally:
    print ("All operations done")
    
# Raising an exception:
#----------------------

def calculate_xFactor(age):
    if age <=0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age

try:
    calculate_xFactor(-1)
except ValueError as error:
    print(error)