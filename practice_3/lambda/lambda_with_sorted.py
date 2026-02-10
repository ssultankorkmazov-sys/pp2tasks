#Sort a list of tuples by the second element:

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#Sort strings by length:

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Sort full names by last name
names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
sorted_by_last = sorted(names, key=lambda s: s.split()[-1])
print("Sorted by last name:", sorted_by_last)

# Case-insensitive sort
fruits = ["banana", "Apple", "cherry", "apricot"]
sorted_ci = sorted(fruits, key=lambda s: s.lower())
print("Case-insensitive sort:", sorted_ci)

# Sort a list of dicts by a numeric field
products = [{"name": "pen", "price": 1.2}, {"name": "notebook", "price": 2.5}, {"name": "eraser", "price": 0.5}]
sorted_products = sorted(products, key=lambda p: p["price"])
print("Products sorted by price:", sorted_products)