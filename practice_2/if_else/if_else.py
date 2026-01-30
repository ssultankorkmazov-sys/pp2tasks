a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Checking even or odd numbers:

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Validating user input:

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")