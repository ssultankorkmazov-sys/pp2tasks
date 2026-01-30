#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#Using the range() function:
for x in range(6):
  print(x)

#Using the start parameter:
for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")