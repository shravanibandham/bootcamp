#requesting the user to enter a sentence
string=input("please enter a string: ")
#splitting the sentence into words using split function
split_string=string.split(' ')
#printing the each word of the sentence on a separate line 
join_string="\n".join(split_string)
print(join_string)