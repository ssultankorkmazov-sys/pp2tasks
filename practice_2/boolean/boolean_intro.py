#Booleans represent one of two values: True or False:
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

'''
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

