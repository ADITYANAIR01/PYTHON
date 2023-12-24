# set is a collection unordered,unindexed & no duplicate items can be used 
# To create a set we have to use a variable_name{"items"}
groceries  =  {"Spices", "Milk", "Noodles"}
drinks     =  {"Coca Cola", "Pepsi", "Cofee"} 

# To add an item to the set use set_name.add
groceries.add("Cereal")

# To remove an item of the set use set_name.remove
groceries.remove("Milk")

# To combine the two sets use set_name.update(Name of set to be included)
groceries.update(drinks) # works either way 

# To combine the two sets in one variable use new_set_name = set1.union(set2)
Buy_list = groceries.union(drinks) # works either way 

# To compare the sets use print(set_name.difference(set_name))
print(groceries.difference(drinks))

#To print all the items in the set
# for x in groceries:
#   print(x)

# To print all the items that are combined in the set
for y in Buy_list:
   print(y)

# To clear the set use use variable_name.clear()
# groceries.clear()