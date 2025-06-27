
# NOTE : In python with operators we can work with simple data types like int , string ..etc ., But cannot work
# with objects . So to use operators like add, subtract etc., with objects we use magic methods and write the code 
# inside the method to work with operators.

class student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self , other_obj):
        m1 = self.m1 + other_obj.m1
        m2 = self.m2 + other_obj.m2
        s3 = student(m1,m2)
        return s3
    
    
s1 = student(1,2)
s2 = student(1,2)

s3 = s1 + s2

print(s3.m1)