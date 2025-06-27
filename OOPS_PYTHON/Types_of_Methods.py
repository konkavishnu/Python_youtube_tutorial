class student :
    
    school = "MCC" # --> this is a class variable
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 =m2
        self.m3 =m3
        
    def avg(self):
        return(self.m1 + self.m2 + self.m3 / 3)
    
    @classmethod  # --> decorators are used to declare a method as class method . We can use these types of methods if we like to work or manipulate the class variables
    def get_School_info(cls): # --> here 'cls' is a keyword like 'self' which represents the class , we need to metion for a class method
        return cls.school 
    
    @staticmethod  # --> these are static methods and it belongs to class and can be called without creating a class
    def info():
        print("This is student Object")
    


s1 = student(1,2,3)

print(s1.avg())

print(s1.get_School_info())

print(student.get_School_info())

student.info()


# NOTE : the difference between "class methods" and "Static method" is that static methods cannot
# modify the class variables , but class methods can modify . Both belong to the class and not to the object.

