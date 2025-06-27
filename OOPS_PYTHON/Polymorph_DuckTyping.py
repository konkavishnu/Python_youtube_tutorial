#                                POLYMORPHISM IN PYTHON
#                                     |
#      _______________________________|_______________________________________
#     |              |                           |                            |
#   DUCK       OPERATOR OVERLOADING        METHOD OVERLOADING          METHOD OVERRIDING
#  TYPING     


# NOTE : Duck typing is we can create object of any class and pass it as argument to a method of a any class ,
# provided that the object of the class passed as argument has the method called in the another method of a class.
# In the below example we have "execute()" method in both the classes so we can create the object of those classes
# and pass it as argument to the "code()" method of the class "Lappy" , since the "code()" method calls "execute()"

class A_ide:
    
    def execute(self):
        print("this is A")

class B_ide:
    
    def execute(self):
        print("this is B")

class Lappy:
    
    def code(self , ide):
        ide.execute()
        
     
   
Lap_1 = Lappy()

ide = A_ide() # or ide = B_ide() 



Lap_1.code(ide)

