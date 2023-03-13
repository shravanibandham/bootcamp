#requesting user the start_year and the no. of years wanted to verify

start_year=int(input("What year do you want to start with? "))
end_year=int(input("How many years do you want to check? "))
#loops for no.of years and checks whether it is a leap year or not and prints accordingly
for i  in range (1,end_year+1):
    if start_year%4==0:
        print(f"{start_year} is a leap year")
    else:
        print(f"{start_year} isn't a leap year")
    start_year+=1       
