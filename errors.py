# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")  #added a parantheses to remove syntax error
#corrected indentation and adding parentheses which are syntax error
print ("\n")
#throws an error that 'ageStr' is not defined. so, corrected it with single'=' instead of '=='
ageStr = "24" #I'm 24 years old.
age = int(ageStr)#agestr cannot be casted as it is a string. So changed it to 24
print("I'm" + str(age) + "years old.")#print function takes only string but 'age' is an integer. so casted it into string. 
three = "3.5"# To get correct answer i changed the value of "three" to 3.5

answerYears = age + float(three)#cannot add integer and string. casting 'three' into float.

print ("The total number of years:" + str("answerYears"))#missing parantheses and casting 'answerYears' into string type
answerMonths = answerYears * 12#'answer' variable not found so changed it into 'answerYears' 
print (f"In 3 years and 6 months, I'll be  {answerMonths} months old") #missing parantheses and formattted into string using f-string

#HINT, 330 months is the correct answer
