num1=int(input("Enter a number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter  third number: "))
avg=(num1+num2+num3)/3
new_num1=0
new_num2=0
new_num3=0
if(num1>avg):
    new_num1=num1
elif (num2>avg):
    new_num1=num2
else:
    new_num1=num3
if (new_num1==num1):
    if num2<num3:
        new_num2=num3
        new_num3=num2 
    else:
        new_num2=num2
        new_num3=num3

if (new_num1==num2):
    if num1<num3:
        new_num2=num3
        new_num3=num1 
    else:
        new_num2=num1
        new_num3=num3    
if (new_num1==num3):
    if num1<num2:
        new_num2=num2
        new_num3=num1
    else:
        new_num2=num1
        new_num3=num2             

print(new_num1,new_num2,new_num3)