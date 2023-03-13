# Requests the user to input a string
string=input("Please enter a string: ")

# Creates a dictionary to store the number of occurences corresponding to each character in the user string

frequency={}

# Checks the number of occurences of each character in the string and adds them to dictionary 
for element in string:
    if element in frequency:
        frequency[element]+=1
    else:
        frequency[element]=1    

# Prints the number of character occurences in a string        
print(f"Occurence of each character in {string} is \n")
print(frequency)        