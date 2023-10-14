import math
def area():
    r=int(input("What's the radius? "))
    print("Area of circle is",math.pi*(r**2))
    l,b=int(input("What's the length? ")),int(input("What's the breadth? "))
    print("Area of rectangle is",l*b)
