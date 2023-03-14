# POLYMORPHISM
# 1.Duck Typing
# class pycharm:
#     def execute(self):
#         print("Compiling")
#         print("Running")
# class myeditor:
#     def execute(self):
#         print("Spell Check")
#         print("Conventional Check")
#         print("Compiling")
#         print("Running")
# class student:
#     def code(self,ide):
#         ide.execute()
# ide=myeditor()
# student1=student()
# student1.code(ide)

class pycharm:
    def execute(self):
        print("Currently you are under pyCharm")
class vsStudio:
    def execute(self):
        print("Currently you are under vsStudio")
class student():
    def code(self,ide):
        ide.execute()

ide=vsStudio()
s1=student()
s1.code(ide)

























