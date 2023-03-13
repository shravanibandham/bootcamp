#intialising contents ,names, dob as an empty string and lists
contents=''
#Opening dob.txt file in a read and write mode
f=open('dob.txt','r+')
names=[]
dob=[]
#Reading the contents from dob.txt file and splitting the names and dates in to their respective lists
for line in f:
    contents=line.split()
    name=contents[0]+' '+contents[1]
    names.append(name)
    dates=contents[2]+' '+contents[3]+' '+contents[4]
    dob.append(dates)
#print(dobcontents)   
#Displaying names and dob from dob.txt file
print("Name\n")
for i in range(0,len(names)):
    print(names[i])
print("\nBirthdate\n")    
for i in range(0,len(dob)):
    print(dob[i])





f.close()
  