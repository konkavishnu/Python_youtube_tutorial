#                               SINGLE INHERITANCE
#                               ******************
class A :
    
    def feature_1(self):
        print("F1")
        
    def feature_2(self):
        print("F2")
        

class B(A): # --> this mentions that class B is child class of 'A' or extends 'A'
    
    def feature_3(self):
        print("F3")
        
    def feature_4(self):
        print("F4")
        
b1 = B() # --> this object b1 can access all the features of A and B


#                          MULTIPLE INHERITANCE
#                         *********************

class A :
    
    def feature_1(self):
        print("F1")
        
    def feature_2(self):
        print("F2")
        

class B(A): # --> this mentions that class B is child class of 'A' or extends 'A'
    
    def feature_3(self):
        print("F3")
        
    def feature_4(self):
        print("F4")
        
class C(A,B):
    
    def feature_5(self):
        print("F5")
        

C1 = C() # --> this will have the features of A , B , C - since C is a child class of B which inturn a child class of A


