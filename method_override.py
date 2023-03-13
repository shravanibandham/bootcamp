# Creates a class that initialises name, age, eye_colour,hair_colour
class Adult:
    def __init__(self,name,age, eye_colour, hair_colour):
        self.name = name
        self.age = age 
        self.eye_colour = eye_colour 
        self.hair_colour = hair_colour

    # Defines a method can_drive() to display persons name and whether he can drive
    def can_drive(self):
        print(f"{self.name} can drive as he is old enough to drive")  


# Creates a subclass Child to super class Adult and initialises name, age, eye_colour,hair_colour
class Child(Adult):
    def __init__(self,name,age,eye_colour, hair_colour):
        super().__init__(name,age,eye_colour,hair_colour)

    # Defines a method can_drive() to display persons name and whether he can drive
    def can_drive(self):
        print(f"{self.name} -  you are too young to drive")


# Requests user to input name, age , eye_colour and hair_colour
name = input("Please enter your name : ")        
age = int(input("Please enter your age : "))
eye_colour = input("Please enter your eye colour : ")
hair_colour = input("Please enter your hair colour : ")

# Creates a object of either parent class or child class depending on the age the user entered and displays whether he can drive
if age >= 18:
    obj = Adult(name, age, eye_colour, hair_colour)
    obj.can_drive()

else:
    obj = Child(name, age, eye_colour, hair_colour)  
    obj.can_drive()  
