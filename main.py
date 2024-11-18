# Inventory is a dictionary of the items in a supermarket and its price
inventory = {
    "Eggs": 2.5,
    "Banana": 3,
    "Milk": 1.25
}

# Item_dict is a dictionary of the items you want to buy and the units
item_dict = {
    "Eggs": 2,
    "Milk": 3
}

# Here we create the function named price_check using the inventory and item_dict as parameters
def price_check(inventory, item_dict):
    # We create a dictionary named shopping_list where we are going to add the item we want to buy and the price for all the units
    shopping_list = {}
    # We loop through all the items in a list created from the items in item_dict
    for i in item_dict.items():
        # We get the item
        item = i[0]
        # We get the units we want to buy
        units = i[1]
        # We get the price of the item from the inventory
        price = inventory.get(item)
        # We add the item and the price for all the units in the dictionary shopping_list
        shopping_list[item] = {price*units}
    # We return the dictionary
    return shopping_list

# Now we use the function price_check
shopping_list = price_check(inventory, item_dict)

# We create a list to add all the prices
total_price = []
# We create a loop through all the items in the dictionary shopping_list
for i in shopping_list.items():
    # We add the price of all the units of the item to the list total_price
    total_price += i[1]
# We check whether the sopping_list is empty or not
if sum(total_price) > 0:
    # Finally we send the final price of the shopping_list
    print(f"The total price of your shopping list is: {sum(total_price)} euros")
else:
    # We send this message in case you don't have anything to buy
    print("You don't have anything in your shopping list")
