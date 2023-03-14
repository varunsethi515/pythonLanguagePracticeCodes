# POLYMORPHISM
#METHOD OVERLOADING
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student(58,85)
print(s1.sum(3,4,5))
print(s1.sum(3,4))
print(s1.sum(3))

#METHOD OVERRIDING
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
a=A()
a.show()
b=B()
b.show()
#When ever you will call the show method it will call the show method of the child class if it has
#else it will print the show method of the parent class



