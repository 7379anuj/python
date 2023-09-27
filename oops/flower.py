class Flower:
    def __init__(self):
        self.root= 1
        self.stem=1
        self.leaves=None
    def flowername(self,name):
        print("Flower name is",name)
    
    def colour(sefl,colour):
        print("colour of flower is",colour)
    def parts(self):   
        print("Flower have roots",self.root)
        print("Flower have stems",self.stem)
        print("Flower have leaves",self.leaves)
    def flowerage(self,age):
        print("Age of flower is ",age)




rose=Flower()
rose.flowername("rose")
rose.colour("red")
rose.parts()
rose.flowerage( 23)

lotus=Flower()
lotus.flowername("Lotus")
lotus.colour("Pink")
lotus.parts()
lotus.flowerage(30)