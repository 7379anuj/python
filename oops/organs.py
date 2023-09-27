class Person:
    def __init__(self):
        self.eyes=2
        self.hand=2
        self.nose=1
    def myname(self,name):
        print("My name is",name)
    def organs(self):
        print("Eyes are",self.eyes)
        print("hand are",self.hand)
        print("Nose are",self.nose)
    def table(self,num):
        self.print_thing="Your table number is"
        print(self.print_thing,num)
        
obj=Person()
obj2=Person()
obj3=Person()

obj.myname("Anuj")
obj2.organs()
obj3.table()