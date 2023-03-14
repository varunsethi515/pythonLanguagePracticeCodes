# class student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#         self.lap=self.laptop()
#     def show(self):
#         print(self.name,self.roll)
#         self.lap.show()
#
#         class laptop:
#             def __init__(self,brand,model):
#                 self.brand=brand
#                 self.model=model
#             def show(self):
#                 print(self.brand, self.model)
#
# s1=student('varun',51)
# s2=student('muskan',15)
# s1.show()
# s2.show()
# lap1=student.lap('HP','Notebook')
# lap2=student.lap('HP','Pavalion')


class Color:
    def __init__(self):
        self.name = 'Green'
        self.lg = self.Lightgreen()
    def show(self):
        print('Name:', self.name)
class Lightgreen:
    def __init__(self):
        self.name = 'Light Green'
        self.code = '024avc'
    def display(self):
        print('Name:', self.name)
        print('Code:', self.code)
outer = Color()
outer.show()
g = outer.lg
g.display()