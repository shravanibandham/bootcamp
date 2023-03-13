import math

def min_numbers(numbers):
    return (min(numbers))

def max_numbers(numbers):
    return(max(numbers))

def avg_numbers(numbers):
    average=sum(numbers)/len(numbers)
    return average
        
f=open("input_numbers.txt","r")
content=[]
list1=[]
f1=open("output.txt","w")
f1.close()
for line in f:
    content=line.split(": ")
    numbers=content[1].replace("\n","")
    list1=numbers.split(",")
    list2=[]

    for item in list1:
        list2.append(int(item))
    if content[0]=="min":
        min_input=min_numbers(list2)
        f1=open("output.txt","a+")
        f1.write( f"The min of {list2} is {min_input}\n")
        f1.close()
    elif content[0]=="max":
        max_input=max_numbers(list2)
        f1=open("output.txt","a+")
        f1.write( f"The max of {list2} is {max_input}\n")
        f1.close()
    elif content[0]=="avg":
        avg_input=avg_numbers(list2)
        f1=open("output.txt","a+")
        f1.write( f"The avg of {list2} is {avg_input}\n")
        f1.close()

f.close()
