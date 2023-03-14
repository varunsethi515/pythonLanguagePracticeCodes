class A:
    def function1(self):
        print('function 1 is working')
    def function2(self):
        print('function 2 is working')
class B(A):
    def function3(self):
        print('function 3 is working')
    def function4(self):
        print('function 4 is working')
class C(B):
    def function5(self):
        print('function 5 is working')
a1=A()
a2=A()
b1=B()
b2=B()
b3=B()
c1=C()
c2=C()
c3=C()
c4=C()
c5=C()
a1.function1()
a2.function2()
b1.function1()
b2.function2()
b3.function3()
c1.function1()
c2.function2()
c3.function3()
c4.function4()
c5.function5()

