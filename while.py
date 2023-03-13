#initializes number_of_digits,number,sum =0
number_of_digits=0
number=0
sum=0
#loops until the user enters -1, calculates the average of user entered numbers and prints the average
while number!=-1:
    number=int(input("please enter a number:"))
    sum= sum+number
    number_of_digits+=1

sum+=1
number_of_digits-=1
average=sum/number_of_digits    

print(f"The average of {number_of_digits} digits you entered is {average} ")    
