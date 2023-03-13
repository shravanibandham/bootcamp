def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])       #changed parameter to 'key' instead of 'k' in dictionary


# creating an empty list to pop the last item to get the desired output
list1=[]
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}


# Appending keys to the list as we need to pass keys as an argument to the print_values_of()
for keys in simpson_catch_phrases:
    list1.append(keys)
list1.pop()    

# changing the second parameter of print_values_of() as we need to pass only two arguments  
print_values_of(simpson_catch_phrases, list1)

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''