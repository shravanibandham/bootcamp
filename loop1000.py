#creates the number_list and adds numbers 1 to 1000 into it
number_list=list(range(1,1001))
#prints the number_list
print(number_list)
print("\nThe even numbers from 1 to 1000 are: \n")
#Prints the even numbers from 1 to 1000
for i in range(len(number_list)):
    if number_list[i]%2==0:
        print(number_list[i],end=' ')