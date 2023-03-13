#Requesting user to enter the price of the product and the distance to send the courier
item_price=float(input("Enter the price of an item: "))
distance=int(input("Enter the distance in Kms: "))
delivery_cost=0.00
#Requesting user to enter whether he want to deliver the courier by air or freight irrespective of case-sensitive 
delivery=input("please enter you want to deliver by air or freight: ")
delivery=delivery.lower()

#calculating the delivery cost depending on the user input as air or frieght. Else error encounters and exits from the loop   
if delivery== 'air':
    delivery_cost=0.36*distance
elif delivery=='freight':
    delivery_cost=0.25*distance
else:
    print("error occured: please enter only \'air\' or \'freight\'")  
    exit()  

#Requesting user to opt b/w limited insurance or full insurance

insurance=(input("please enter do you want limited insurance or full insurance: "))
insurance=insurance.lower()
#calculating the insurance cost depending on the user input as limited insurance or 'full insurance'. Else error encounters and exits from the loop
if insurance=='limited insurance':
    insurance_cost=25
elif insurance=='full insurance':
    insurance_cost=50
else:
    print("error occured: please enter only 'limited insurance' or 'full insurance")
    exit()

#Requesting use to select whether it is a gift or not and calculating cost accordingly
 
send_gift=input("please enter is it a gift or not. If yes,please enter yes else no ")
send_gift=send_gift.lower()
if send_gift=='yes':
    gift_price=15
else:
    gift_price=0

#Requesting the user to select the delivery type and calculating its cost accordingly

delivery_type=input("please enter do you wnat a standard delivery or Priority: ")
delivery_type=delivery_type.lower()
if delivery_type=='standard':
    delivery_type_cost=20
elif delivery_type=='priority':
    delivery_type_cost=100
else:
    print("please enter only 'standard' or 'priority' ")
    exit()

#Calculating the total price depending on the user input
total_price=item_price+delivery_cost+insurance_cost+gift_price+delivery_type_cost
print(f"The total price for your delivery is {total_price}")




