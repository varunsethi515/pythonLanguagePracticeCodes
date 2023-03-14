#CREATING CLASS, METHOD AND OBJECT OF THAT PARTICULAR CLASS
class Computer_Science_Engineering: #CREATING CLASS
    def Student_Details(self):  #CREATING METHOD OF THE CLASS COMPUTER_SCIENCE_ENGINEERING
        print("Varun Sethi, 12017951, Handsome Hunk")
        print("Sweet and Innocent Guy")
Comp1=Computer_Science_Engineering()    #CREATING OBJECT1 OF THE CLASS COMPUTER_SCIENCE_ENGINEERING
Comp2=Computer_Science_Engineering()    #CREATING OBJECT2 OF THE CLASS COMPUTER_SCIENCE_ENGINEERING
# Computer_Science_Engineering.Student_Details(Comp1) #CALLING OBJECT1
# Computer_Science_Engineering.Student_Details(Comp2) #CALLING OBJECT2
Comp1.Student_Details() #CALLING OBJECT1
Comp2.Student_Details() #CALLING OBJECT2

#CREATING VARIABLES OF THAT PARTICULAR CLASS
class K20HS:
    def __init__(self, name, reg_no): #ACTUALLY __INIT__ IS A CONSTRUCTOR
        self.name=name
        self.reg_no=reg_no
    def student_record(self):
        print("Configuration of your Computer is", self.name, self.reg_no)
Student1=K20HS("Intel i5",16)
Student2=K20HS("AMD Ryzen 5",8)
Student1.student_record()
print(id(Student1))
Student2.student_record()

#USE OF SELF IN DETAIL AnD CONSTRUCTOR
class Person:
    def __init__(self):
        self.name="Varun Sethi"
        self.age=21
    def compare(self,other):    #COMPARE( WHOME TO COMARE, WITH WHOME TO COMPARE )
        if self.age==other.age:
            return True
        else:
            return False
    def update(self):
        self.age=21
P1=Person()
P2=Person()
P1.name="Kiddo"
P2.age=20
P2.update()
print(P1.name,P1.age)
print(P2.name,P2.age)
print(P1.compare(P2))   #P1.COMPARE(P1,P2) / P1.COMPARE(SELF,P2) => SELF=P1




