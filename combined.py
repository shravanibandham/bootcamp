# Requests user to enter the number of integers to enter into numbers1.txt file
integers=int(input("Please enter number of integers you want to enter into numbers1.txt file: "))
numbers=[]
numbers2=[]
# opens numbers1.txt file and writes sorted integers into it
f1=open("numbers1.txt","w+")

for i in range(0,integers):
    
    num=int(input("enter the integer: "))
    numbers.append(num)
numbers.sort()
for i in range(0,len(numbers)):
    f1.write(str(numbers[i])+"\n")

# Requests user to enter the number of integers to enter into numbers2.txt file
integers2=int(input("Please enter number of integers you want to enter into numbers2.txt file: "))
# opens numbers2.txt file and writes sorted integers into it
f2=open("numbers2.txt","w+")

for i in range(0,integers2):
    num=int(input("enter the integer: "))
    numbers2.append(num)
numbers2.sort()
for i in range(0,len(numbers2)):
    f2.write(str(numbers2[i])+"\n")    
f1.close()           
f2.close()
# opens numbers1.txt, numbers2.txt file and all_numbers.txt file
f1=open("numbers1.txt","r")
f2=open("numbers2.txt","r")
f3=open("all_numbers.txt","w+")
# reads the integers from numbers1.txt file and numbers2.txt file and stores in 'contents' list
contents=[]
for line in f1:
    contents.append(int(line))
for line in f2:
    contents.append(int(line)) 
contents.sort()         #sorts the 'contents' list

# Writes the sorted integers from numbers1.txt and numbers2.txt files into all_numbers.txt file

for i in range(0,len(contents)):
    f3.write(str(contents[i])+"\n")

# Closes all the files to free the resources
f3.close()
f2.close()
f1.close()