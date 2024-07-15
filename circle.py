import math

class Circle:

  def __init__(self, radius):

    self.radius = radius

  def getArea(self):

    return math.pi * self.radius**2

  def getCircumference(self):

    return 2 * math.pi * self.radius

circle1 = Circle(5)
area = circle1.getArea()
circumference = circle1.getCircumference()

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
