class Student():
    Class = 10
    def __init__(self,m1,m2,m3):
        self.m1=m1 #INSTANCE METHOD
        self.m2=m2
        self.m3=m3
    def average(self):# INSANCE METHOD
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self): #IT WILL FETCH THE VALUE ACCESSOR INSTANCE METHOD
        return self.m1
    def set_m1(self,value): #IT WILL UPDATE THE VALUE TOO MUTATORS INSTANCE METHOD
        self.m1=value
    @classmethod #DECORATOR
    def get_class(cls):#CLASS METHOD
        return cls.Class
    @staticmethod#DECORATOR
    def info():#STATIC METHOD
        print("This is Student class and Static Method")

s1=Student(91,92,35)
s2=Student(25,100,100)
print(s1.average())
print(s2.average())
print(Student.get_class())
Student.info()
