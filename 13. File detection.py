# First import os 
import os

# create a variable ="address" use \\ instead of \
path = "C:\\Users\\adity\\Documents\\PDF\\HELLO.txt"

# use if else statements for checking if the file mentioned is there 
if os.path.exists(path):
    print("The location exist!")
else:
    print("The location does not exist ")