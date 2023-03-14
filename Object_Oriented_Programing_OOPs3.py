#NESTED CLASS / CLASS INSIDE A CLASS
class student:
    def __init__(self, name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop: #INNER CLASS OF STUDENT
        def __init__(self,brand,ram,processor):
            self.brand='HP'
            self.ram=8
            self.processor='I5'
        def show(self):
            print(self.brand, self.ram, self.processor)

s1=student("Varun" , 515)
s2=student("Muskan", 142)
s1.show()
lap1=s1.lap
lap2=s2.lap
lap3=student.laptop()


