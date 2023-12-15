# Set is a collection of data that is unordered,unindexed & has no duplicate values
stationery = {"Pencils", "Pen", "Eraser", "NoteBook"} # in sets we use curly brackets{}

School_essentials = {"Water bottles", "Lunch boxes", "Geometry boxes"}

stationery.add("Refill")          # To add something to a set
stationery.remove("Pencils")     # TO remove something from a set
# stationery.clear()            # To clear the set

# To add two sets to each other use .update method
# stationery.update(School_essentials)

# To add two sets with a new variable using .union method
School = stationery.union(School_essentials)

# To find the difference between two sets
# print(stationery.difference(School_essentials))


for x in School: # To print all the data in set
    print(x)