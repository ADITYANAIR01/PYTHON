try:
    with open('Network_config.txt')as file:
        print(file.read())

# first write with open('file name ') as file then print print(file_name.read())
except FILENOTFOUNDERROR:
    print("The file was not found ")