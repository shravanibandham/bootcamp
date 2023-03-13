# Requesting user to enter how many students are registering

number_of_students=int(input("Please enter the number of students you want to register: "))
# Opening a file reg_form.txt to write the students id

f = open("reg_form.txt",'w+')
# Looping for the amount of students and writing their id's into the file

for i in range(0,number_of_students):
    id=input("Please enter your id: ")
    f.write(id +"\t \t--------------\n")

f.close()
# Prints the content of reg_form.txt file
f1=open("reg_form.txt","r")
for line in f1:
    print(line)
# Closing the opened file to free the resources   
f1.close()