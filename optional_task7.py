#Requesting the user to enter select whether the employee is salesperson or manager
Employee_type=input("please enter whether the employee is salesperson or manager:  ")
Employee_type=Employee_type.lower()

#calculating the total salary of a salesperson if the user input is salesperson 
if Employee_type=='salesperson':
    gross_sales=float(input("please enter the gross sales repective to employee: "))
    commission = (gross_sales*8)/100
    fixed_salary=2000
    total_salary=commission+fixed_salary
    print(f"Your monthly wage is {total_salary}")

#calculating the total salary of manager if the user input is manager
elif Employee_type=='manager':
    hours=float(input("please enter the no. of hours worked: "))
    salary=40*hours
    print(f"your monthly wage is {salary}")

#Displaying error if user enters invalid input and exits
else:
    print("Error occured: please enter only either 'manager' or 'salesperson'") 
    exit()  
