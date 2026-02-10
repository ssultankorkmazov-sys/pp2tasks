# Filter out even numbers from a list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Filter words longer than 3 characters
words = ["apple", "bat", "car", "dog", "elephant"]
long_words = list(filter(lambda w: len(w) > 3, words))
print("Words with length > 3:", long_words)

# Filter a list of dicts (keep adults age >= 18)
people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 15},
    {"name": "Diana", "age": 22}
]
adults = list(filter(lambda p: p["age"] >= 18, people))
print("Adults:", adults)