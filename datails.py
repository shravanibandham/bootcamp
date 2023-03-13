# requesting user to input name, age, house number and street name
name=input("enter your name: ")
age= int(input("enter your age: "))
house_number=int(input("enter your house number: "))
street_name= input("enter your street name : ")
#printing the details of the user  using f-string
print(f"This is {name} who is {age} years old, lives at {house_number} on {street_name}")
#printing the details of the user using .format method
print("This is {} who is {} years old, lives at {} on {}".format(name,age,house_number,street_name))