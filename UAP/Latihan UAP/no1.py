data = [2, 4, 1.1, 9, 5.0, 71, 3.3, 1.2, 20, 23, 0.5]

list_integers = [x for x in data if isinstance(x, int)]
tuple_floats = tuple(x for x in data if isinstance(x, float))

print("List of integers:", list_integers)
print("Tuple of floats:", tuple_floats)
