#declaring a variable and assigning a string to it
hero="$$$Superman$$$"
#Removing $ at the beginning and at the end of string
print("Before stripping the string is "+hero)
print("After stripping the string is ",end='')
print(hero.strip('$'))