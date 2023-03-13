#Requesting user to enter a string
string=input("please enter a string: ")
i=0
string1=""
#printing the user entered string such that each alternate character is uppercase and alternate character is lowercase
for i in range (0,len(string)):
    if i%2==0:
        string1=string1+string[i].lower()
    else:
        string1=string1+string[i].upper()
print(f" The original string is {string}")
print(f" The converted string is {string1}")        
#splitting the string into words
split_string=string.split(' ')
#printing the string such that alternate word is uppercase and alternate word is lowercase
for i in range(0,len(split_string)):
    if i%2==0:
        split_string[i]=split_string[i].upper()
    else:
        split_string[i]=split_string[i].lower()
#print(split_string)            

join_string=" ".join(split_string)
print(f" The alternate string is {join_string}")          
