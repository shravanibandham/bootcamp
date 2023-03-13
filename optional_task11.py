contents=''
characters=0
words=0
char_count=0
f=open('input.txt','r')
for line in f:
    contents=line.split()
    words+=len(contents)
    for j in (0,len(contents)-1):
      characters =characters+len(contents[j])
    #for k in range(0,len(contents)):
while 1:
     
    # read by character
    char = f.read(1) 
    char=char.lower()        
    if not char:
        break     
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        char_count+=1
print(f"The no of words are {words}")    
print(f"The no of chracters are {characters}")
print(char_count)