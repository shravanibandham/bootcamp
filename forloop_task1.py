#Requesting user to enter a number of which times table to print
number=int(input("please enter a number: "))
#loops 12 times and prints the user given "number's" times table
for i in range(1,13):
    print(f"{number} * {i} = {number*i}")
