class vehicle :
    
    def __init__(self, make, model):  # --> constructor to pass the value
        self.make = make
        self.model = model
         
    
    def moves(self):
        print("Moves along....")
        
    def get_make_model(self):
        print(f"I'am a {self.make} {self.model}.")
    
  
my_car = vehicle('Tesla','Model_3') # ---> object creation with class "vehicle"

my_car.moves()  # --> calling the function inside the class

print(my_car.make)
print(my_car.model)
print(my_car.get_make_model())