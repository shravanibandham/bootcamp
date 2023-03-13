# Creates the dictionary with abbreviation and its meaning
meaningOfAbbreviation={
    'ADSL' : 'Asymmetric Digital subscriber line',
    'API': 'Application Programming Interface',
    'IDE': 'Integrated Development Environment',
    'GUI': 'Graphical User Interface'
    }

# Adds two more elements into th dictionary
meaningOfAbbreviation['SDK']= 'Software Development Kit'
meaningOfAbbreviation['SSH']= 'Software Shell'

# Requests user to enter the abbreviation,he wanted the meaning for
shortform=input("Please enter an abbreviation you want the meaning for: ").upper()

# checks whether user entered abbrievation is in the list
# If it is prints the meaning else displays meaning not found
if shortform in meaningOfAbbreviation:
    print(f"The meaning of {shortform} is ",end='' )
    print(meaningOfAbbreviation[shortform])
else:
    print("Abbreviation not found.")    