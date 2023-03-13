# Program demonstrting logical error 

print("STEM Career advisor")
print("-------------------")

print("Q1: Would you like to work:")
print("1) Mostly indoors")
print("2) Mostly outdoors")
answer = input("[1/2]: ")

if answer == "1":
  print("Q2: Do you love animals?")
  print("1) Yes")
  print("2) NO")
  if answer == "1":
    print("You an work as a veteran")