class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * (self.radius **2) * self.height

    def surface_area(self):
        return (2 * self.pi) * self.radius * (self.radius + self.height)
        
height = int(input("Enter height value: "))
radius = int(input("Enter radius value: "))
c = Cylinder(height,radius)
print("Surface area",c.volume())
print("Surface area",c.surface_area())