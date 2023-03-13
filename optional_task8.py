#Requests the user to enter a number 
number=int(input("please enter a number: "))

#loops until the user enters the number that is less than 100 
#if user enters an even number then it multiplies by 2 else multiplies it by 3 and prints the result
while number>100:
    number=int(input("please enter a number that is less than 100: "))
    continue
if number%2==0:
    number=number*2
    print(number)
else:
    number=number*3
    print(number)    