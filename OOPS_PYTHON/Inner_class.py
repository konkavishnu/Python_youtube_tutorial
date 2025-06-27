class Student :
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() # ---> Here we are assigning the laptop obj as variable to the class student
        
    def show(self):
        print(self.name ,self.rollno)
        print(self.lap.show()) # --> here we are calling the method of the inner class via the variable(lap) of the outer class
        
    
    class Laptop :
        
        def __init__(self):
            self.brand = "ASUS"
            self.cpu = "Ryzen"
            self.ram = 16
            
        def show(self):
            return(self.brand,self.cpu,self.ram)


s1 = Student("Vishnu", 22)

Laptop = s1.Laptop() # --> here we are creating a separate obj called laptop with the inner class .
                           # NOTE : inner class obj cannot be created unless called by the outer class obj - In this case we are 
                           # calling via the outer class obj "s1".

