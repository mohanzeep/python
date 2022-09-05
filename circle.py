import math
def area_of_the_circle(r):
    area=r**2*math.pi
    return area
radius=float(input("plese enter the radius of given circle:"))
print("the area of given circle is:",area_of_the_circle(radius))
