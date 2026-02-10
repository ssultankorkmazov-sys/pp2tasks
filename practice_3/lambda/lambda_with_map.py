#Double all numbers in a list:

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Square each number
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Sum elements from two lists (map with multiple iterables)
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))
print("Pairwise sums:", sums)

# Convert Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print("Fahrenheit:", fahrenheit)

# Format list of dicts to strings