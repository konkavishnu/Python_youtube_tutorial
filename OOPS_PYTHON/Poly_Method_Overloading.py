
# Python does not support method overloading in the traditional sense, unlike languages like Java 
# or C++ where you can define multiple methods with the same name but different parameter lists 
# (different number or types of arguments).In Python, if you define multiple methods with the 
# same name within a class, the last defined method will effectively "override" any previously 
# defined methods with the same name.


# However, you can achieve similar functionality to method overloading in Python using various techniques:

# Default Arguments:
# ******************
# You can define a single method with default values for some parameters. 
# This allows the method to be called with different numbers of arguments, where the missing arguments 
# will take their default values.

class MyClass:
    def greet(self, name="Guest", greeting="Hello"):
            print(f"{greeting}, {name}!")

obj = MyClass()
obj.greet()          # Output: Hello, Guest!
obj.greet("Alice")   # Output: Hello, Alice!
obj.greet("Bob", "Hi") # Output: Hi, Bob!


# Variable-length Arguments (*args and `: kwargs`):** 
#**************************************************
# You can use *args to accept a variable number of positional arguments and **kwargs to 
# accept a variable number of keyword arguments. You can then use conditional logic within 
# the method to handle different argument combinations.

class Calculator:
    def add(self, *args):
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return args[0] + args[1]
        else:
            return sum(args)

calc = Calculator()
print(calc.add(5))         # Output: 5
print(calc.add(5, 10))     # Output: 15
print(calc.add(1, 2, 3, 4)) # Output: 10


# Conditional Logic and Type Checking:
#*************************************
# Within a single method, you can use isinstance() or other 
# checks to determine the type of arguments passed and perform different operations accordingly.

class Processor:
    def process(self, data):
        if isinstance(data, int):
            print(f"Processing integer: {data}")
        elif isinstance(data, str):
            print(f"Processing string: {data}")
        else:
            print(f"Processing unknown type: {type(data)}")

proc = Processor()
proc.process(10)
proc.process("hello")
proc.process([1, 2])
