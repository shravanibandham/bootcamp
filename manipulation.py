str_manip=input("enter a string: ")
#finding the length of the string
length=len(str_manip)
print(length)
#finding the last character of the string 
char=str_manip[length-1:length]
print("the last character of the string is: "+char)
#replacing the letter with @
replace_sentence=str_manip.replace(char,'@')
print(replace_sentence)
#prints last three characters of a string
print(str_manip[-3:])
#finding first three letters of a string
sub_string=str_manip[:3]
#finding last two letters of a string
sub_string1=str_manip[-2:]
print(sub_string+sub_string1)
#spliting the string
new_string=str_manip.split(" ")
#print(new_string)
#joining the splitted string and printing in a separate line
join_string="\n".join(new_string)
print(join_string)
