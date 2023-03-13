#creates friends_names list and asks the number of friends want to enter.

friends_names=[]
number=int(input("please enter how many friends names you want to enter: "))
#appends the list with friends names
for i in range(0,number):
    name=input("Please enter your friends name: ")
    friends_names.append(name)
#prints friends names 
print(friends_names)
#prints first and last friend's name
print(friends_names[0])
print(friends_names[len(friends_names)-1])    
#prints the length of friends_names
length=len(friends_names)
print(f"The length of the list is {length}")
#loops until the length of friends_names and asks to corresponding friends name and age
#If user enter coressponding name and age then adds age to the list
#Else throws an error and exits out of the loop
friends_ages=[]
for i in range(length):
    friends_name=input("please enter the name of the friend you want to enter their's age: ")
    if friends_name==friends_names[i]:
        age=input("please enter your friend's age: ")
        friends_ages.append(age)
    else:
        print("Error occured in entering corresponding friend's name: ")
        break
#print(friends_ages)
#Prints the friends names and their ages if all the ages are entered else displays only the entered ages
if len(friends_names)==len(friends_ages):

    for i in range(length):
        print(friends_names[i]+ ":" + friends_ages[i])
else:
    print("You didn't enter all of your friend's ages")
    print("You entered only these ages:\n")
    for i in range(len(friends_ages)):
         print(friends_names[i]+ ":"+ friends_ages[i])       