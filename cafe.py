# Creates the list of items
menu=['tea','coffee','cake','chocolate']
totalvalue=0

# creates a dictionary that contains stock value of each item in the menu
stock={
    'tea':'3',
    'coffee':'4',
    'cake':'5',
    'chocolate':'6'
    }

# Creates the dictionary that contains price of each item in the menu
price={
    'tea':1.24,
    'coffee':1.45,
    'cake':2.50,
    'chocolate':3.00
}

# Calculates the total value of the stock and prints it
for i in range(0,len(menu)):
    name=menu[i]
    value=float(stock[name])*float(price[name])
    totalvalue+=value
totalvalue=round(totalvalue,3)
print(f"The total value of the stock is {totalvalue}")