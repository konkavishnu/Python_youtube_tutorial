class vehicle :
    # NOTE : here 'self' is the instance of the class vehicle
    
    color ="yellow"
    
    # MAGIC METHODS : any method with starting with "_" and end with "_" . 
    # These methods are directly called by python interpreter , without being called or defined.
    
    def __init__(self, make, model):  # --> constructor to pass the value
        self.make = make
        self.model = model
        
    def __str__(self): 
        return f"({self.make},{self.model})"
      
    @classmethod   # --> we to mention this decorator or annotations to mention this is a factory method . Factory methods can be accessed directly without creating the object.  
    def zero(cls): # --> these are same as static methods in java , these do not belong to the instance / obj but to the class. These are also known as "Factory methods"
         print("this is classmethod")
    
    def moves(self):
        print("Moves along....")
        
    def get_make_model(self):
        print(f"I'am a {self.make} {self.model}.")
    
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # NOTE : class level attributes are all shared with all instances of the class.
 # For example if there is a attribute "color" with string "yellow" . When we manipulate the value 
 # as vehicle.color = "red" , then the other objects created with class vehicle will have red as color
 # rather than yellow.
 
vehicle.color = "red" 


vehicleObj = vehicle('Skoda','Enyaq')

vehicleObj.make = 'Volkswagen' 

  
  
my_car = vehicle('Tesla','Model_3') # ---> object creation with class "vehicle"
print(my_car.color)
isinstance(my_car , vehicle) # --> used to find whether the created obj is instance of the class.

my_car.moves()  # --> calling the function inside the class


print(my_car.make)
print(my_car.model)
print(my_car.get_make_model())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#                               MAGIC METHODS
#                               -------------

# To compare two objects:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, otherObj): # --> Magic method to check for equal
        return self.x == otherObj.x and self.y == otherObj.y
    
    
    
    
NewObj = Point(1,2)
OtherObj = Point(1,2)
print(NewObj == OtherObj)