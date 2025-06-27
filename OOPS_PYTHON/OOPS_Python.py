class Computer:
    
    # NOTE : "SELF" is the instance of the created object
    
    # def __init__(self,CPU,RAM): # --> like constructor and needs to be written on top of all methods of the class
    #     print("in init")
    #     self.CPU = "Ryzen"
    #     self.RAM = 16
    
    def __init__(self): 
        print("in init")
        self.CPU = "Ryzen"
        self.RAM = 16
    
    def config(self):
        print("Config is : ", self.CPU ,self.RAM)
        
    def update(self):
        self.RAM = 32
        
    def compare(self,other):
        if self.RAM == other.RAM:
            print("equal")
        else:
            print("Not equal")    
        
    
        

# com_1 = Computer("i5","16gb")
# com_2 = Computer("i7","8gb")

com_1 = Computer()
com_2 = Computer()

com_1.config() #---------> This same as calling - Computer.config(com_1) - behind compiler this happens
com_2.config() 

com_1.compare(com_2)



# Computer.config(com_1)
# Computer.config(com_2)


print(type(com_1))

