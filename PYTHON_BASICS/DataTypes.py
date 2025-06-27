import math
#                                                  STRING DATA TYPE
#                                                  -----------------
first = "Vishnu"
last = "Vardhan"
print(type(first))  # --> will tell you what is the datatype of that value
print(type(first) == str)  # --> will check if the correct datatype or not
print(isinstance(first, str))  # --> will check if 'first' is an instance of a String Object
# Constructor Function :
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation :
fullname = first + " " + last
fullname += "!"
fullname = "Super" + fullname  # --> to add string to the beginning
print(fullname)

# Type Casting :
decade = str(1234)
print(type(decade))

# Multiple Lines :
multiline = ''' Hello World
This is a good multiline string
'''
print(multiline)

# Escaping Special characters :
sentence = 'I\'m back at work !\t Hey!\n\nWhere\'s this at\\located ?'
print(sentence)

# String Methods :
print(first.lower())
print(first.upper())
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
print(len(multiline))
multiline = "   " + multiline
multiline += "    "
print("The length of multiline is : ", len(multiline))
print("The length of multiline now after removing whitespaces is : ", len(multiline.strip()))
print(multiline.lstrip())  # --> removes leading whitespaces
print(multiline.rstrip())  # --> removes trailing whitespaces

# Build Menu :
title = "menu".upper()
print(title.center(20, "="))  # --> centre keyword will print the String in Centre
print("Coffe".ljust(16, ".") + "$1".rjust(4))  # --> "ljust" is left justify , "rjust" is right justify
print("Muffin".ljust(16, ".") + "$10".rjust(4))
print("Cake".ljust(16, ".") + "$15".rjust(4))

# String Index Values
print(first[0])  # --> returns the value of the index
print(first[-1])  # --> first.length - 1
print(first[0:-1])  # --> this will return the range of values starting from index zero to the INDEX BEFORE THE END-INDEX mentioned
print(first[0:])  # --> this will return the range of values starting from index zero to last index .

# Some methods return boolean data
print(first.startswith("V"))
print(first.endswith("U"))

#                                  BOOLEAN DATA TYPE
#                                  ------------------
myValue = True
x = bool(myValue)
print(type(myValue))
print(isinstance(myValue, bool))

#                                  NUMERIC DATA TYPE
#                                  -----------------
price = 100  # --> Integer
print(type(price))
print(int(price))
print(isinstance(price, int))

gpa = 3.28  # --> Float
comp_value = 5 + 3j  # --> complex
print(type(comp_value))
print(comp_value.real)  # --> prints only 5.0
print(comp_value.imag)  # --> prints only 3.0

print(abs(gpa))
print(round(gpa))  # --> this will round off normally
print(round(gpa, 1))  # --> this will round off to the specified decimal point

# We need to declare "import math" & use math function
print(math.pi)
print(math.cos(3))
