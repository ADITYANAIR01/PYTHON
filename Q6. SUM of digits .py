# Create a program to calculate the sum of the digits of a given number.

def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    digits = str(number)
    
    # Sum the individual digits
    digit_sum = sum(int(digit) for digit in digits)
    
    return digit_sum

# Example usage:
num = 12345  # You can replace this with any number for which you want to find the sum of digits
result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}")


   