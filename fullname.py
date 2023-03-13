#Reuesting user to enter fullname
full_name=input("Enter your full name: ")
#calculate the length of fullname
length=len(full_name)
#check whether user entered fullname or not and print accordingly
if length==0:
    print("You haven't entered anything.Please enter your fullname.")
elif length<4:
    print("You have entered less than 4 characters. Please make sure you have entered your fullname.")
elif length>25:
    print("You have entered more than 25 characters. Please make sure that you have entered only your fullname.")
else:
    print("Thank you for entering your fullname!")    
