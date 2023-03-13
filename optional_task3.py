#requesting two values from the user and storing the values in the variables num1,num2
num1=int(input("enter a number: "))
num2=int(input("enter second number: "))
print("Before swaping the values of num1 and num2 are:")
print(num1)
print(num2)
# Taking a temporary variable called "temp" and storing the value of "num1" into it and the swaping the value of "num1" with "num2" and "num2" with temp
temp=num1
num1=num2
num2=temp
print("After swaping the values of num1 and num2 are: ")
print(num1)
print(num2)
