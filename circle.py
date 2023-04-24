'''Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.'''

class circle():
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        return (pi*(self.radius**2))
    def getcircumference(self):
        return (2*pi*self.radius)
pi=3.14
r=float(input("Enter radius of circle: "))
obj=circle(r)
a=obj.getarea()
cr=obj.getcircumference()
print("Area of circle:",a)
print("Perimeter of circle:",cr)
