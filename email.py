class Email:
    def __init__(self,from_address,subject_line,email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        has_been_read = False
        is_spam = False
    def mark_as_read(self):
        self.has_been_read = True   
    def mark_as_spam(self):
        self.is_spam = True

class Inbox(object):
    def __init__(self):
        self.emails = []   
    def add_email(self,from_address,subject_line,email_contents):
        #email1 = Email(from_address, subject_line, email_contents)
        emails.append(Email(from_address, subject_line, email_contents))
        #print(emails[0].from_address)
        
class Test:
    Inbox.add_email("shravani.bandham@gmial.com", "test2", "test contents")
    print(emails)