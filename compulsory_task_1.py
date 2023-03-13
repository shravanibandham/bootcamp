# Create a class that defines the contact_details() and location()
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def location(self):
        print("The head office location is at Capetown")  


# Create a subclass OOPCourse to main class Course and defines trainer_details()
class OOPCourse(Course):
    def __init__(self):
    
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"  

    def trainer_details(self):
        print("The course name is ", self.description)
        print("The trainer name is : ", self.trainer )

    def show_course_id(self,id):
        self.id = id
        print("The course id is : ", self.id) 



# Prints the contact details and course details using subclass object
course_1 = OOPCourse()    
course_1.contact_details ()
course_1.location()
course_1.trainer_details ()
course_1.show_course_id(12345)