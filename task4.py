#Requesting user to enter an integer
number=int(input("please enter an integer: "))

# verifing whether number is divisible by 2 or 5 or 2 and 5 or not divisible 2 and 5 
if number%2==0 and number%5==0:
    print(f"Your number {number} is divisible by 2 and 5")
elif number%2==0 and number%5!=0:
    print(f"Your number {number} is divisible by 2")
elif number%2!=0 and number%5==0:
    print(f"Your number {number} is divisible by 5")
else:
    print(f"Your number {number} is  not divisible by 2 and 5")           
