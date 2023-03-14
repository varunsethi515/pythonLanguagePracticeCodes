class A:
    def __init__(self):
        print("__init__ of ClassA")
    def function1(self):
        print('function 1 is working')
class B:
    def __init__(self):
        print("__init__ of ClassB")
    def function2(self):
        print('function 2 is working')
class C(A,B):
    def __init__(self):
        super().__init__()  #super() method is used to print the init method of parent class
        print("__init__ of ClassC")
    def function3(self):
        print('function 3 is working')
c1=C()
#  why the init method of class b is not printed?
#  because of MOR method resolution order, and it will always get execute  from left to right

#first of all it will look for the init method in it's own class if we will be able to find the init so it will print that if not then it will search
# for the init method in parents class.