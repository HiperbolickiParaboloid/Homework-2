class Line:
    def __init__ (self, cord1=(0,0), cord2=(0,0)):
        self.cord1=cord1
        self.cord2=cord2
    def slope (self):
        return (self.cord1[1]-self.cord2[1])/(self.cord1[0]-self.cord2[0])
    def distance(self):
        return (((self.cord1[0]-self.cord2[0])**2)+((self.cord1[1]-self.cord2[1])**2))**(0.5)
k=Line((3,2),(8,10))
print(k.slope())
print(k.distance())