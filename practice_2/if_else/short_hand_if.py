#One-line if statement:
a = 5
b = 2
if a > b: print("a is greater than b")

#One-line if/else that prints a value:
a = 2
b = 330
print("A") if a > b else print("B")

#one-line if/else to choose a value and assign it to a variable:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#One line, three outcomes:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Setting a default value:
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
