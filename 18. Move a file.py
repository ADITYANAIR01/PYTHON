import os 

source = "HI.txt"
destination  = "C:\\Users\\adity\\Downloads"

try:
    if os.path.exists(destination):
        print("There is already the file there ")
    else:
        os.replace(source, destination)
        print(source+" the file was moved ")
except FileNotFoundError:
    print(source+" was not found ")