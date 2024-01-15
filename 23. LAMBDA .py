# lambda function are anonmous written in 1 line using lambda keyword 
# that accepts any argument  but can only have one expressions 

double = lambda x:x*2 # double 
print(double(10))

add = lambda x,y:x+y  # int
print(add(5,4))

name = lambda first_name, last_name:first_name + " " + last_name  # str
print(name("Aditya","Nair"))