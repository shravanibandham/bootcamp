fav_rest=input("enter your favourite restaurant: ")
int_fav=int(input("enter your favourite number"))
print(fav_rest)
print(int_fav)
cast_string=int(fav_rest)
#throws a "ValueError" as it cannot convert a non-convertible string into an integer 
print(cast_string)