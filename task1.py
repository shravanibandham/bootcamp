#Assigning and declaring variables num1,num2,num3
num1=int(input("please enter a number: "))
num2=int(input("please enter second number: "))
num3=int(input("Please enter third number: "))
#checking whether numm1 or num2 is greatest
if num1 >num2:
    print(f"{num1} is greater than {num2}")
else: 
        print(f"{num2} is greater than {num1}")

#finding whether num1 is even or odd
if num1 % 2==0 :
    print(f"{num1} is an even number")
else:
    print(f"{num1} is an odd number")

#sorting num1,num2,num3 in an descending order

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





