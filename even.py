#Requesting user to enter a number
number=int(input("please enter a number: "))
iterator=1
#loop iterates until iterator<=number and prints even numbers 
while iterator<=number:
     
    if iterator%2==0:
        print(iterator)
    iterator+=1


