#declaring and assinging float value to variable num1, integer to num2, integer to num3, string value to string1
num1=99.23
num2=23
num3=150
string1="100"
print("before conversion: ")
#Didn't know how to print multiple statements in a single line. so, took the help of google
print(f"The value of num1 is {num1} and its type is ", end='')
print(type(num1))
print("The value of num2 is {} and its type is ".format(num2),end='')
print(type(num2))
print("The value of num3 is {} ".format(num3),end='')
print(type(num3))
print("The value of string1 is {} and its type is  ".format(string1),end='')
print(type(string1))
#converting num1 to an integer
num1=int(num1)
#converting num2 into float
num2=float(num2)
# converting num3 into a string
num3=str(num3)
#converting string1 into an integer
string1=int(string1)
print("After conversion: ")
#printing the values of num1, num2,num3,string1 and their types
print("The value of num1 is {} and its type is ".format(num1),end='')
print(type(num1))
print("The value of num2 is {}  and its type is ".format(num2),end='')
print(type(num2))
print("The value of num3 is {} and its type is  ".format(num3),end='')
print(type(num3))
print("The value of string is {} and its type is ".format(string1),end='')
print(type(string1))