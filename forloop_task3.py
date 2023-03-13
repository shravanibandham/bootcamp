#Requesting user to enter the number from the no to print reverse of numbers
number=int(input("please enter a number to print reverse of numbers: "))
#prints the numbers in reverse from the user entered number
while number>=0:
    print(number)
    number-=1
#prints the even numbers from 1 to 20    
print("The even numbers from 1 to 20 are: ")
for i in range(1,21):
    if i%2==0:
        print(i)

#prints "*" in aparticular sequence
series=int(input("please enter a number to print a series of stars: "))
for i in range(1,series+1):
    for j in range (1,i+1):
        print("*",end='')
    print("\n")     
        
#finds and prints the GCD of two numbers
print("To find GCD of two numbers: ")
n1=int(input("please enter a number: "))
n2=int(input("please enter second number: "))
while n1!=n2:
    
    if (n1 > n2):
        n1 -= n2
    else:
        n2 -= n1
print(f"GCD of two nunmbers is {n1}")