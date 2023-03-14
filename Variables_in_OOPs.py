#IN OOPs THERE ARE TWO TYPES OF VARIABLE PRESENT 1=>INSTANCE VARIABLE AND 2=>STATIC VARIBLE/CLASS VARIABLE
class car():
    wheels=4    #CLASS VARIABLE SAME FOR LL OBJECT
    def __init__(self):
        self.milage=10  #INSTANCE VARIABLE
        self.company="BMW"
c1=car()
c2=car()
c2.milage=12
car.wheels=5
print(c1.milage,c1.company,c1.wheels)
print(c2.milage,c2.company,car.wheels)
#YOU CAM ACCESS CLASS VARIABLE WTHT THE HELP OF OBJECT NAME OR WITH THE HELP OF CLASS NAME "C1.WHEELS == CAR.WHEELS"
