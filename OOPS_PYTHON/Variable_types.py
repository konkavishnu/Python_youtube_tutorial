class car :
    
    wheels = 4 #-------> These are called "Class variables" (same like static variables), 
               # these are shared among all objects created with the class "car" since 
               # they belong to the class rather than the object. They are declared outside "_init_"
    
    def __init__(self):
        self.milage = 10 # --> These are known as instance variables and are declared inside "_init_"
        self.name ="BMW"
        

car.wheels = 5    # --> since we have changed the value it will affect all objects created with the class "car"    

C1 = car()
C2 = car()

print(C1.wheels)
print(C2.wheels)
        

