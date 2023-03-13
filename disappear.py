#Requesting user to enter a string
string=input("please enter a string: ")
#Requesting user to enter the characters that are to be removed
characters=input("enter the characters  to remove from the word separated by , : ")
#creating a list out of the user entered characters
removal_list=characters.split(",")
#looping in the range of user entered characters list
for i in removal_list:
    new_string=string.replace(str(i),'') #Replacing the character in the string with an empty space
    string=new_string
print(new_string)        