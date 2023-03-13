# Defining min_nmbers() to find min of numbers in the list
def min_numbers(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    print(f"min of {numbers} is {min}")
    return min        


# Defining max_nmbers() to find max of numbers in the list
def max_numbers(numbers):
    max = numbers[0]
    for num  in numbers:
        if num > max:
            max = num
    print(f"Max of {numbers} is {max}")        
    return max        


# Defining avg_nmbers() to find avg of numbers in the list
def avg_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    average = sum / len(numbers)
    print(f"The average of {numbers} is {average}")
    return average
        

# Opening input_numbers.txt file to read contents from it        
f=open("input_numbers.txt","r")
content = []
list1 = []


#Opening output.txt file to write contents into it
f1 = open("output.txt","a+")



# Looping for the number of times the lines in the file and finding the min,max and avg of numbers accordingly
for line in f:
    content = line.split(": ")
    if len(content) == 2:
        numbers = content[1].replace('\n','')
        list1 = numbers.split(",")
        list2 = []

        for item in list1:
            list2.append(int(item))
        
        if content[0] == "min":
            min_input = min_numbers(list2)
            #f1 = open("output.txt","a+")
            f1.write( f"The min of {list2} is {min_input}\n")
            # f1.close()
        
        elif content[0]=="max":
            max_input = max_numbers(list2)
            # f1 = open("output.txt","a+")
            f1.write( f"The max of {list2} is {max_input}\n")
            # f1.close()
        
        elif content[0]=="avg":
            avg_input = avg_numbers(list2)
            # f1 = open("output.txt","a+")
            f1.write( f"The avg of {list2} is {avg_input}\n")
            # f1.close()


# Closing the file to effect the contents in the file
f.close()
f1.close()

print("-----------------\n")
print("The contents of output.txt file is:\n")
print("------------------\n")
with open("output.txt",'r') as f:                            #Displaying the contents of 'output.txt' file
    print(f.read())
