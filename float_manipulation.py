# importing the required libraries
import math
import statistics

# Creating a list of 10 numbers
number_list=[65,42,73.56,82,10,45.32,10,56,32.56,45.63]
total=0

# Calculating the total of numbers and printing it
for i in range(0,len(number_list)):
    total+=number_list[i]
print(f"The total of numbers you entered is: {total}")

# Finding position of maximum number in the list and printing it
max_pos=number_list.index(max(number_list))+1
print(f"The maximum number is {max_pos} position") 

# Finding position of minimum number in the list and printing it   
min_pos=number_list.index(min(number_list))+1
print(f"The minimum number is {min_pos} position")

# Finding median of numbers in the list and printing it
median=statistics.median(number_list)
print(f"The median of numbers in the list is {median}")

