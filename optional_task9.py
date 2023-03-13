#Requests the user to enter a number
number=int(input("please enter a number: "))
#checks whether the user entered a number >10. 
# If yes,prints the number as many times the number user entered.
# Else prints its too small 
if number>10:
    for i in range(1,number+1):
        print(number)
else:
    print("sorry,too small")        