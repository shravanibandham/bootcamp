# Creating a function that prints all the days of the week

def days_of_week():
    print("Sunday\n")
    print("Monday\n")
    print("Tuesday\n")
    print("Wednesday\n")
    print("Thursday\n")
    print("Friday\n")
    print("Saturday")

# Creating a function that takes string as an argument and replaces every second word with "Hello"    
def converted_string(sentence):
    split_string=sentence.split(" ")
    for i in range(0,len(split_string)):
        if i%2==0:
            split_string[i]="Hello"
            
    join_sentence=" ".join(split_string)     
               
    return join_sentence       # Returns the converted string

# calls the function that prints all the days of the week
days_of_week()    

#Requests user to enter a string and passes that string as an argument to function converted_string
string=input("Please enter a string: ")
output=converted_string(string)    

# Prints the coverted string
print(output)