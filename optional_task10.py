#Requesting user to enter a string
string=input("Please enter a string : ")
#Reversing a string using string slicing 
reverse_string=string[::-1]
#checking whether the user entered string is palindrome or not and printing it accordingly.
if string==reverse_string:
    print("your word is Palindrome")
else:
    print("Your word is not a palindrome")    