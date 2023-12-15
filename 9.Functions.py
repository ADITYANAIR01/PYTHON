# Function is block of code that will only run when called
def add ():
    print("input a number ")
    number1 = int(input("Enter 1'st number  "))
    number2 = int(input("Enter 2'nd' number "))
    sum = number1+number2
    print(sum)

def subtract():
    number3 = int(input("Enter 1'st number  "))
    number4 = int(input("Enter 2'nd' number "))
    sum2 = number3-number4
    print(sum2)

print("Welcome to maths function ")
add()
subtract()
