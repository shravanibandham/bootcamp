#Reuesting user to enter swimming,cycling and running times
swimming_time=float(input("Please enter the swimming time completed in mins: "))
cycling_time=float(input("Please enter the cycling time completed in mins: "))
running_time=float(input("Please enter the running time completed in mins: "))

#calculating total time to determine the user cutoff time
total_time=swimming_time+cycling_time+running_time

#Awarding the user accordingly based on their cutoff times.
if total_time<=100:
    print("You've been awarded PROVINCIAL COLOURS")
elif total_time>100 and total_time>=105:
    print("You've been awarded PROVINCIAL HALF COLOURS")
elif total_time>105 and total_time>=110:
    print("You've been awarded PROVINCIAL SCROLL")
else:
    print("Sorry no award this time. Better luck next time")           