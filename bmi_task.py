#Requesting user to enter their height and weight
weight=float(input("Please enter your weight in kg:  "))
height=float(input("Please enter your height in meters "))
#Calculating user BMI and displaying whether they are obese,over weight, normal or under weight depending on their BMI
bmi = (weight)/(height*height)
print(f"Your BMI is  {bmi}")
if bmi>=30:
    print("You are obese. Please take care of your weight.")
elif bmi>=25:
    print("You are overweight. Be cautious.")
elif bmi>=18.5:
    print("You have normal BMI. Well done!")
else:
    print("You are underweight. Please try to put on your healthy weight.")            
