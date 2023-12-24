# First import os 
import os

# create a variable ="address" use \\ instead of \
path = "C:\\Users\\adity\\Documents\\PDF\\folder"

# use if else statements for checking if the folder  mentioned is there 
if os.path.isdir(path):
    print("The location of the folder exist!")
else:
    print("The location of the folder does not exist ")