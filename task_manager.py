# Imports datetime library
from datetime import datetime
# ====Login Section====
'''
Here you will write code that will allow a user to login.
    - Reads usernames and password from the user.txt file
    - Uses dictionary to store a list of usernames and passwords from the file.
    - Uses a while loop to validate  user name and password.
    - If user is validated, menu is displayed for the user to select an option
'''

user_name=input("Please enter the username: ")
valid_password=input("Please enter the password: ")
user_list={}

f= open("user.txt",'r+')
for line in f:
    content=line.split(", ")
    user_list.update({content[0]:content[1].strip("\n") })  


while True:
    if user_name in user_list:
        
        p=str(user_list[user_name])
        
        while valid_password!=p:
            valid_password=input("please enter a valid password : ")
        break            
    else: 
        user_name=input("Please enter valid username :") 
        continue  
print("Please select an option from following menu: \n")

'''
     - If user is validated, menu is displayed for the user to select an option
     - Register user and display statistics are displayed only if the user is admin
'''

if user_name=="admin":
   print("r- Register user\n")
   print("ds- Display no.of users and tasks")
print("a- Adding a task\n")
print("va- View all tasks\n")
print("vm- View my tasks\n")
print("e- Exit")
menu=input("Please enter an option: ").lower()
f.close()
#print(menu)

# If user selects 'r' from the menu and the user is admin the following code registers user 
# and writes username and password to user.txt file
if menu=='r' and user_name=="admin":
    new_username=input("Please enter the username: ")
    f= open("user.txt","r")
    user=[]
    for line in f:
        content=line.split(", ")
        user.append(content[0])
    while new_username in user:
        new_username=input("username already exists. Please enter the new username: ")
        if new_username in user:
            break
    new_password=input("Please enter the password: ") 
    confirm_password=input("Please confirm the password: ")
    while confirm_password!=new_password:
        print("password didn't match\n")
        new_password=input("Please enter the Password: ")
        confirm_password=input("Please confirm the Password: ")
    f=open("user.txt","a+")    
    f.write("\n"+new_username+", " +new_password)
    f.close()


# If user selects 'ds' from the menu then the number of tasks and number of users will be displayed.
elif menu=='ds' and user_name=="admin":
    with open("tasks.txt","r") as f:
        user=[]
        tasks=[]
        for line in f:
            content=line.split(", ")
            user.append(content[0])
            tasks.append(content[1])
        user_count=[]
        for i in user:
            if i not in user_count:
                user_count.append(i)
    print(user_count)
    print(tasks)
    print(f"The total number of users are: {len(user_count)}")
    print(f"The total number of tasks are: {len(tasks)}")            

            

# If user selects 'a' from the menu,new task will be assigned to the user and writes the details to tasks.txt file
elif menu == 'a':
    f=open("tasks.txt","a+")
    user=input("Please enter the username to whom the task has to be assigned: ")
    title=input("Please enter the title of the task: ")
    task_description=input("Please the task description: ")
    due_date=input("Please enter the due date in dd-mmm-yyyy format: ")
    assign_date=datetime.now()
    status="NO"
    entry= user+", "+title+", "+task_description+", "+due_date+", "+assign_date+","+status+"\n"
    #print(entry)
    f.write(entry)
    f.close()


# If the user selects 'va' option from the menu,all the tasks will be displayed.
elif menu == 'va':
    f=open("tasks.txt","r")
    task_list=f.readlines()
    for line in task_list:
        split_data=line.split(", ")
        display="------------------------------------------------------------\n"
        display+=f"assigned to :\t {split_data[0]}\n"
        display+=f"Task:\t{split_data[1]}\n"
        display+=f"Description: \t {split_data[2]}\n"
        display+=f"Assigned date:\t {split_data[3]}\n"
        display+=f"Due date:\t {split_data[4]}\n"
        display+=f"Task complete:\t {split_data[5]}\n"
        display+="------------------------------------------------------------\n"
        print(display)
        f.close()


# If the user selects 'vm' from the menu, then all the tasks related to the user will be displayed
# If the user has no tasks assigned, then the relative message will be displayed
elif menu== 'vm':
    user_task_list=[]
    f=open("tasks.txt","r")
    for line in f:
      user_task={}
      content=line.split(", ")
      #print(content)  
      if len(content)==6:
         user_task.update({"username":content[0]})
         user_task.update({"task":content[1]})
         user_task.update({"Description":content[2]})
         user_task.update({"AssignedDate":content[3]})
         user_task.update({"DueDate":content[4]})
         user_task.update({"Taskcomplete":content[5]})
         user_task_list.append(user_task)
    #print(user_task_list)  
    user_found=False  
    for i in range(0,len(user_task_list)):
        temp=user_task_list[i]
        #print(temp.get("username"))
        if temp.get("username")==user_name:
            
            for key,value in temp.items():
                print(key, ':', value)
            user_found=True
    if user_found==False:
        print("No tasks were assigned to user")
    f.close()   


# If user selects 'e' then he will be exited by displaying the message 
elif menu=="e":
    print("Good Bye!")
    exit()


# If the user enters any options other than mentioned in the menu then 'invalid option' message will be displayed.
else:
    print("You entered invalid option")                 
