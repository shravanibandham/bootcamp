#creates a name list and adds names to list until user enters 'john' irrespective of case sensitivity

name_list=[]
name=input("Please enter your name: ")
name=name.lower()
while name!='john':
    name_list.append(name)
    name=input("please enter your name: ")
    name=name.lower()
#prints out the list of names
print("\nThe names in the list are: \n")
print(name_list)    