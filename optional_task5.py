#importing math to support mathematical funtions
import math
#Requesting user to enter the sides of a triangle
side1=int(input("enter the side1 of a triangle: "))
side2=int(input("enter the side2 of a triangle: "))
side3=int(input("enter the side3 of a triangle: "))
#calculating area of a triangle
s=(side1+side2+side3)/2
print(s)
sub_area=s*(s-side1)*(s-side2)*(s-side3)
print(sub_area)
area=round(math.sqrt(sub_area),2)
print("The area of the triangle is: "+ str(area))