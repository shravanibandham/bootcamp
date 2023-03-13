#importing datetime to access the date and time  
import datetime 
currentDate = datetime.date.today()
current_year=currentDate.year

#requesting user year of birth
year=int(input("enter your year of birth:  "))
#calculating age of the user
age=current_year-year
print(f"your age is {age}")
#checking whether user age is above 18.If yes allowing to enter else not
if age>=18:
    print("congrats you are old enough to enter.")
elif age>16 and age<18:
    print("Almost there!")
elif age<=16:
    print("Sorry You're just too young to enter.")
else:
    print("please enter a valid year. ")        
