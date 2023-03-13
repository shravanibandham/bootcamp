#creates a movie list and adds the movie names in to the list

movies_list=[]
number=int(input("Please enter the number of movie names you want to enter: "))
for i in range(0,number):
    movie_name=input("Please enter the movie name: ")
    movies_list.append(movie_name)
#Displays the movies names in the list 
for i , movies in enumerate(movies_list,start=1):
    print("movie "+str(i),movies)
    #print(f"movie {i+1} : {movies_list[i]}")
