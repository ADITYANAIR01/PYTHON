# list is used to store multiple items in a single variables 
# To start making list for name the variable & put different items in []

food = [ "Pizza", "Burger", "Hot dog", "Chocolate brownie"]

# To acess a certain item print(variable name[index f item ])
print(food[0])

# To replace an item on list use variable name[index number to be replaced = "the item to be listed in"]
food[0]= "Noodles"

# To add an item on the list use variable_name.append("item name ")
food.append("ice cream")

# To remove an item of the list  use variable_name.remove("item name ")
food.remove("Hot dog")

# To pop i.e remove the last element on the list use variable_name.pop("item name ")
food.pop()

# To insert an item a value in a certain index
food.insert(2, "Ratatouli" )

# To remove all the elements of an list use variable_name.clear()\
# food.clear()

# To list all the items in the list 
for i in food:
    print(i)
