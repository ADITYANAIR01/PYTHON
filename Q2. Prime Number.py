# Write a program in Python to find if a number is prime or not

number = 12

is_prime = True

for i in range(2, number):
   if number % i == 0:
       is_prime = False
       break

if is_prime:
   print(f"{number} is a prime number.")
else:
   print(f"{number} is not a prime number.")
