#Creating an empty list to store the user entered names of the pupils
names=[]
string=''
#loop iterates until the user enters 'stop' and prints the number of names user entered.
while string!='stop':
    string=input("please enter a name of the pupil :")
    names.append(string)
print(len(names)-1)        
