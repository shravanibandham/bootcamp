#importing math library to use maths functions
import math
#Requesting user to enter the shape of the building irrespective of case-sensitive
shape=input("please enter your building shape as square, rectangle or round:  ")
shape=shape.lower()

#calculating area of building depending on the user input
if shape=='square':
    length=float(input("please enter length : "))
    area=math.pow(length, 2)
    print(f"The area of your square bulding with length {length} is {area}sqm")
elif shape=='rectangle':
    length=float(input("please enter the length: "))
    breadth=float(input("please enter the breadth : "))
    area=length*breadth
    print(f"The area of your rectangular building with length {length} and width {breadth} is {area}sqm")
else:
    radius=float(input("please enter the radius: "))
    area=math.pi*math.pow(radius,2) 
    print(f"The area of your circular building with radius {radius} is {area}sqm")       