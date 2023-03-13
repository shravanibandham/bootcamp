import math
#Requesting user to enter three product names
product1=input("enter the  first product name: ")
product2=input("enter the  second product name: ")
product3=input("enter the  third product name: ")
#Requesting user to enter the price of the products and rounding up its value to two decimal places
price1=round(float(input("enter the first product price: ")),2)
price2=round(float(input("enter the second product price: ")),2)
price3=round(float(input("enter the third product price: ")),2)
#calculating total price of the products and printing its value
total_price=price1+price2+price3
print("The total price of the products is: "+ str(total_price))
#finding the average price of the products and printing its value
avg_price=(total_price/3)
print("the average price of the products is: "+ str(round(avg_price,2)))
print(f"The total of {product1},{product2},{product3} is {total_price} and the average of the items is {avg_price}")
