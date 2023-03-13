# Creates a function to calculate the hotel cost taking number of days as an argument
def hotel_cost(nights):
    total_cost=nights*100
    return total_cost

# Creates a function to calculate the flight cost taking name of city as an argument
def plane_cost(city):
    city=city.lower()
    if city=='paris':
        total_cost=500
    elif city=='rome':
        total_cost=600
    elif city=='venice':
        total_cost=700
    return total_cost
 
# Creates a function to calculate the car hire cost taking number of days as an argument 
def car_rental(days):
    total_cost=days*50
    return total_cost

# Creates a function to calculate the total holiday cost taking cost of the hotel,plane cost and car cost as arguments
def holiday_cost(hotel,city,car):
    total_cost=hotel+city+car
    return total_cost

# Requests user to input to enter the no. of days to stay in hotel,the city to go and the no. of days wanted car rental 
# calls the functions accordingly and calculates the total holiday cost
no_of_nights=int(input("Please enter the number of days you want to stay in hotel: "))
cost_of_hotel=hotel_cost(no_of_nights)
city_name=input("Please enter the among Paris,rome, venice cities you want to go: ")
cost_of_plane=plane_cost(city_name)
car_hire=int(input("Please enter the no.of days you want to hire the car: "))
cost_of_car= car_rental(car_hire)
total_holiday_cost=holiday_cost(cost_of_hotel, cost_of_plane, cost_of_car)
print(f"The cost of hotel for {no_of_nights} days is {cost_of_hotel}\n")
print(f"The cost of flight for {city_name} is {cost_of_plane}\n")
print(f"The cost of car hire for {car_hire} days is {cost_of_car}\n")
print(f"The total cost for holiday is {total_holiday_cost}")