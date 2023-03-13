# Imports datetime library
import datetime
import os.path

def reg_user():
   # If user selects 'r' from the menu and the user is admin the following code registers user 
    # and writes username and password to user.txt file
    #if menu=='r' and user_name=="admin":
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


# If the user selects 'a' from the menu the following function is called and adds the tasks to the user
def add_task():
    f=open("tasks.txt","a+")
    user=input("Please enter the username to whom the task has to be assigned: ")
    title=input("Please enter the title of the task: ")
    task_description=input("Please the task description: ")
    format_date=input("Please enter the due date in dd-mmm-yyyy format: ")
    due_date=datetime.datetime.strptime(format_date,'%d %b %y')
    assign_date=str(datetime.datetime.now().strftime('%d %b %y'))
    status="NO"
    entry= user+", "+title+", "+task_description+", "+due_date+", "+assign_date+", "+ status + "\n"
    #print(entry)
    f.write(entry)
    f.close()


# If the user selects 'va' from the menu the following function is called and displays all the tasks
def view_all():
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


# If the user selects 'vm' from the menu then the following function is called and displays the tasks related to the user
# and also asks the user to select from the menu whether he want to edit due date or Mark the task as complete
# If the user select to edit due date i.e choice 1, then edits due date
# If the user selects to Mark the task as complete i.e choice 2, then edits the task as complete
def view_mine(user_name1):
    i=1
    data=[]
    f=open("tasks.txt","r")
    user_found=False
    print(user_name1)
    for line in f:
       
       content=line.split(", ")
       print(content[0])  
       if content[0]==user_name1:
           
           display=f"--------------------------{i}----------------------------------\n"
           display+=f"assigned to :\t {content[0]}\n"
           display+=f"Task:\t{content[1]}\n"
           display+=f"Description: \t {content[2]}\n"
           display+=f"Assigned date:\t {content[3]}\n"
           display+=f"Due date:\t {content[4]}\n"
           display+=f"Task complete:\t {content[5]}\n"
           display+="------------------------------------------------------------\n"
           print(display)
           i+=1
           user_found=True
           
       data.append(content)
           
           
    if user_found==False:
        print("No tasks are assigned to user")    
    f.close()
    
    while True:
        task_choice=int(input("Please select a task number you want to edit:"))
        if task_choice<=0 or task_choice>len(data):
            print("You have selected an invalid option,try again:")
            continue
        edit_data=data[task_choice-1]
        break
    while True:
        tasks_write=open("tasks.txt","w+")
        output=f'select an option:\n'
        output +='1:Edit due date\n'
        output+= '2:Mark as completed\n'
        choice=int(input(output))
        if choice<=0 or choice>=3:
            print("You have selected an invalid option,try again")
            continue
        elif choice==1:
            edit_data[-2]=input("Please edit your due data in dd-mmm-yyyy format: ")
            print(edit_data)
            new_data=", ".join(edit_data)
            for line in data:
                new_line=", ".join(line)
                tasks_write.write(new_line)
        elif choice==2:
            #split_data=edit_data.split(", ")
            #split_data[-1]='Yes\n'
            edit_data[-1]='Yes\n'
            #new_data=", ".join(split_data)
            new_data=", ".join(edit_data)
            for line in data:
                new_line=", ".join(line)
                tasks_write.write(new_line)
        tasks_write.close()
        #tasks_read.close()
        

        print("You have finished the task!")
        break          

        
# If the user selects 'ds' from the main menu and if the user is admin, then the following function generates reports
def generete_reports():
    task_file=open("tasks.txt","r")
    task_list=task_file.readlines()
    task_file.close()
    overdue=0
    complete=0
    uncomplete=0
    total=0

    # calculates the total no. of tasks , overdue tasks ,completed tasks and incomplete tasks
    # calculate the percentages of uncompleted tasks and overdue tasks and writes the contents to task_overview.txt file 
    for line in task_list:
        data_list=line.split(", ")
        #print(data_list)
        total+=1
        #print(line)
        if data_list[5].lower()=='no':
            uncomplete+=1
            due_date=data_list[-2]
            date_obj = datetime.datetime.strptime(due_date, '%d %b %Y')
            current_date=datetime.datetime.today().strftime('%d %b %Y')
            current_date1=datetime.datetime.strptime(current_date, "%d %b %Y")
            
            if date_obj < current_date1:
                overdue+=1
        else:
            complete+=1
            uncomplete+=1
        percent_complete=(complete/total)*100
        percent_uncomplete=(uncomplete/total)*100
        percent_overdue=(overdue/total)*100    
        # print(total)
        # print(percent_complete)
        # print(percent_uncomplete)
        # print(percent_overdue)

    #print(f"uncompleted tasks : {uncomplete} and overdue tasks : {overdue}")
    with open('task_overview.txt','w') as task:
        task.write(f"uncompleted tasks: {uncomplete}\noverdue tasks: {overdue}\ncompleted tasks: {complete}")
        task.write(f"percentage of completed tasks: {percent_complete}\n")
        task.write(f"percentage of uncompleted tasks: {percent_uncomplete}\n")
        task.write(f"percentage of overdue tasks: {percent_overdue}\n")
    
    
    # Creates a dictionary of completed tasks of each user and stores the user and no. of tasks completed related to the user as a key, value pair
    # Creates a dictionary of incompleted tasks of each user and stores the user and no. of tasks completed related to the user as a key, value pair
    # Creates a dictionary of overdue tasks of each user and stores the user and no. of tasks completed related to the user as a key, value pair
    # Creates a dictionary of total tasks of each user and stores the user and no. of tasks completed related to the user as a key, value pair
    total_tasks_of_user={}
    complete={}
    incomplete={}
    overdue_tasks={}
    user_total=0
    with open("tasks.txt","r") as f:
        for line in f:
         content=line.split(", ")
         if content[0] not in complete.keys():

             complete.update({content[0]:0})
         if content[0] not in incomplete.keys():
             incomplete.update({content[0]:0})
         if content[0] not in overdue_tasks.keys():
             overdue_tasks.update({content[0]:0})
         if content[0] not in total_tasks_of_user.keys():
             total_tasks_of_user.update({content[0]:0})
         if (content[5].strip("\n")).lower() == 'no':
             if content[0] in incomplete.keys():
                 no_of_tasks=incomplete[content[0]]
                 incomplete.update({str(content[0]) : no_of_tasks+1}) 
             else:
                 incomplete.update({content[0]:1})
         else:
             if content[0] in complete.keys():
                 no_of_tasks=complete[content[0]]
                 complete.update({str(content[0]) : no_of_tasks+1}) 
             else:
                 complete.update({content[0]:1})
         due_date=content[-2]
         date_obj = datetime.datetime.strptime(due_date, '%d %b %Y')
         current_date=datetime.datetime.today().strftime('%d %b %Y')
         current_date1=datetime.datetime.strptime(current_date, "%d %b %Y")
            
         if date_obj < current_date1:
            if content[0] in overdue_tasks.keys():
                 overdue=overdue_tasks[content[0]]
                 overdue_tasks.update({str(content[0]) : overdue+1}) 
            else:
                overdue_tasks.update({content[0]:1})

        
         user_total = int(incomplete[content[0]]) + int(complete[content[0]])
         #print(f" The total tasks of user {content[0]} and completed tasks are {complete[content[0]]} and incomplete tasks are {incomplete[content[0]]} ")
         total_tasks_of_user.update({content[0] : user_total})
        
        # print(overdue_tasks)       
        # print(incomplete)
        # print(complete)
        # print(total_tasks_of_user)


    # calculates the percentages of tasks completed, incomplete and overdue and writes to  'user_overview.txt' file         
    with open("user_overview.txt","w") as f:
        for key,values in complete.items():
            user_task_percentage = (total_tasks_of_user[key] / total ) * 100
            user_complete_percentage = (complete[key] / total_tasks_of_user[key]) * 100
            user_incomplete_percentage = (incomplete[key] / total_tasks_of_user[key]) * 100
            user_overdue_percentage= (overdue_tasks[key] / total_tasks_of_user[key]) * 100

            f.write(f"user:  {key} \n")
            f.write(f"completed tasks are {complete[key]}\n")
            f.write(f"The no. of incompleted tasks are: {incomplete[key]}\n")
            f.write(f"The no.of overdue tasks are: {overdue_tasks[key]}\n")
            f.write(f"The percentage of total no. of tasks assigned to user is {user_task_percentage}\n")
            f.write(f"The percentage of completed tasks assigned to user is {user_complete_percentage}\n")
            f.write(f"The percentage of incomplete tasks assigned to user is {user_incomplete_percentage}\n")
            f.write(f"The percentage of overdue tasks assigned to user is {user_overdue_percentage}\n")
            f.write(f"--------------------------------------------\n")      


# If the user is admin and selects 'ds' from the menu then the statistics will be displayed.
def display_statistics():
    file_exists = os.path.exists('user_overview.txt')
    if file_exists == 'True' :
        with open('user_overview.txt','r') as f:
            print(f.read())

    else: 
        generete_reports()
        with open('user_overview.txt','r') as f:
            print(f.read())
            
        




# ====Login Section====
'''

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
   print("ds- Display statistics\n")
   print("gr- Generate reports\n")
print("a- Adding a task\n")
print("va- View all tasks\n")
print("vm- View my tasks\n")
print("e- Exit")
menu1=input("Please enter an option: ").lower()
f.close()
if menu1=='r':
    reg_user()
elif menu1=='a':
    add_task()  
elif menu1=='va':
    view_all()
elif menu1=='vm':
    view_mine(user_name)
elif menu1=="gr":
     generete_reports()
elif menu1 == 'ds':
    display_statistics()                  
elif menu1=="e":
     print("Good Bye!")
     exit()


# If the user enters any options other than mentioned in the menu then 'invalid option' message will be displayed.
else:
     print("You entered invalid option")


