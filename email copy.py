# creates a class in which initialiser initialises from_address, subject_line,
# email_contents, has_been_read and is_spam
class Email(object):
    """ generated source for class Email """
    has_been_read = bool()
    is_spam = bool()
    from_address = str()
    subject_line = str()
    email_contents = str()

    def __init__(self):
        self.has_been_read = False
        self.is_spam = False

    def __init__(self, from_address, subject_line, email_contents):
        """ generated source for method __init__ """
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

# Defines a method that sets has_been_read to true 
    def mark_as_read(self):
        """ generated source for method mark_as_read """
        self.has_been_read = True

# Defines a method that sets is_spam to true
    def mark_as_spam(self):
        """ generated source for method mark_as_spam """
        self.is_spam = True


# Creates a class that defines various functionalities of an e-mail 
class Inbox(object):
    emails=[]
    
    
    def __init__(self):
        self.emails=[]
    
    
    # Defines a function that stores all the e-mails
    def add_email(self,from_address,subject_line,email_contents):
        self.emails.append(Email(from_address, subject_line, email_contents))
        
    
    # Defines a function that displays all the e-mails from the particular sender
    def list_messages_from_sender(self,sender_address):
        counter = 0
        for mail in range(0,len(self.emails)):
            if self.emails[mail].from_address == sender_address:
                print(str(counter)+" "+self.emails[mail].subject_line)
                counter = counter+1
    
    
    # Defines a function that displays all the e-mails from a particular sender at the given index
    def get_email(self, sender_address,index):
        counter = 0
        user_index = False
        sender = False
        for mail in range(0,len(self.emails)):
            if self.emails[mail].from_address == sender_address:
                if counter == index:
                    self.emails[mail].has_been_read = True
                    print(self.emails[mail].email_contents) 
                    user_index = True
                counter = counter+1
                sender = True    

        if user_index == False:
            print("Mail not found at that index")    
                
        if sender == False:
            print("sender not found")
    
    
    # Defines a function that marks the e-mail from the sender at given index as spam
    def mark_as_spam(self, sender_address, index) :
        counter = 0
        sender = False
        index = False
        for mail in range(0,len(self.emails)) :
            if self.emails[mail].from_address == sender_address:
                if counter == index:
                    self.emails[mail].is_spam = True
                    index = True
                    #return self.emails[mail]                
                counter = counter+1
                sender = True
        if sender == False:
            print("Sender not found")
        if index == False:
            print("Index not found for the sender")            
    

    # Defines a function that displays all the unread e-mails
    def get_unread_emails(self):
        
        for mail in range(0,len(self.emails)) :
            #print(self.emails[mail].is_spam)
            if self.emails[mail].has_been_read == False:
                print(self.emails[mail].subject_line)

    
    # Defines a function that displays all the spam e-mails
    def get_spam_emails(self):

        for mail in range(0,len(self.emails)) :
            #print(self.emails[mail].is_spam)
            if self.emails[mail].is_spam == True:
                print(self.emails[mail].subject_line)    

    
    # Defines a function that deletes the e-mails from the particular sender at the given index
    def delete(self, sender_address, index) :
        counter = 0
        sender = False
        index = False
        for mail in range(0,len(self.emails)-1) :
            if self.emails[mail].from_address == sender_address:
                if  counter == index:
                    self.emails.remove(self.emails[mail])
                    index = True
                    #return self.emails[mail]                
                counter = counter+1
                sender = True  
        if sender == False:
            print("Sender not found")
        if index == False:
            print("Index not found for the sender")                


# Creates a class that implements all the funtionalities of Email and Inbox
class Test:

    inbox = Inbox()
    
    # Displays the menu for the user to select the operation
    print("Welcome to the email system! What would you like to do?")
    print("Please select an option from below menu:\n")
    print("s - send email.")
    print("l - list emails from a sender.")
    print("r - read email.")
    print("m - mark email as spam.")
    print("gu - get unread emails.")
    print("gs - get spam emails.")
    print("d - delete email.")
    print("e - exit this program.")
    #An Email Simulation

    while True:
        user_choice = input("Please select an option from above menu:  ").strip().lower()
        if user_choice == "s":
            # Sends an email (Create a new Email object)
            sender_address = input("Please enter the address of the sender\n:")
            subject_line = input("Please enter the subject line of the email\n:")
            contents = input("Please enter the contents of the email\n:")

            # Now adds the email to the Inbox

            inbox.add_email(sender_address, subject_line, contents) 
            # Prints a success message
            print("Email has been added to inbox.")

            
        elif user_choice == "l":
            # List all emails from a sender_address
            sender_address = input("Please enter the address of the sender\n:")
            inbox.list_messages_from_sender(sender_address)
            

    
        elif user_choice == "r":
            # Read an email
            # Asks the user to enter the  sender address
            sender_address = input("Please enter the address of the sender of the email\n:")
            
            # Asks the user for the index of the email
            email_index = int(input("Please enter the index of the email that you would like to read\n:"))
            
            # Displays the email of the particular sender at the given index
            inbox.get_email(sender_address, email_index)
            

            
        elif user_choice == "m":
            # Mark an sender email as spam at the given index
            
            sender_address = input("Please enter the address of the sender of the email\n:")

            email_index = int(input("Please enter the index of the email to be marked as spam\n:"))
            inbox.mark_as_spam(sender_address, email_index)
            
            print("Email has been marked as spam")

            
        elif user_choice == "gu":
            # Lists all unread emails
            inbox.get_unread_emails()
            
        elif user_choice == "gs":
            # Lists all spam emails
            inbox.get_spam_emails()
            
        elif user_choice == "e":
            print("Goodbye")
            break
        elif user_choice == "d":
            # Delete an email
            
            sender_address = input("Please enter the address of the sender of the email\n:")
            email_index = int(input("Please enter the index of the email to be deleted\n:"))
            inbox.delete(sender_address, email_index)
            print("Email has been deleted")

        else:
            print("Oops - incorrect input")

        
    