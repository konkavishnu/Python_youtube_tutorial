class A :
    
    def __init__(self):
        print("Construct of A")
    
    def feature_1(self):
        print("F1")
        
    def feature_2(self):
        print("F2")
        

class B(A): # --> this mentions that class B is child class of 'A' or extends 'A'
    
    def __init__(self):
        super.__init__    # --> here we are calling the constructor of the parent class separately
        print("Construct of B") # NOTE : If constructor of B is not defined then it will call the constructor of 
                                # it's super or parent class  
        
    def feature_3(self):
        print("F3")
        
    def feature_4(self):
        print("F4")

        
class C(B,A):
    
    # NOTE : Here C needs to call either Constructor of A or B . In such cases python
    # will follow MRO - Method Resolution order i.e it will go from Left to 
    # right . Here (B,A) so it will call the constructor of B .
    
    def __init__(self):       
        super().__init__()
        # Super(A,self)._init_() --> here we are calling the costructor of A seperately - this type of calling can be done to avoid diamond problem
        print("Constructor of C")  
    
    def feature_5(self):
        print(super().feature_4)
        print(super().feature_2) # --> We can also use Super to call the parent methods
        print("F5")
        
        

C1 = C()
C1.feature_5()
