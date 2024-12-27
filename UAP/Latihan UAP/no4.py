data = [2, 4, 1.1, 9, 5.0, 71, 3.3, 1.2, 20, 23, 0.5]

tuple_floats = tuple(x for x in data if isinstance(x, float))

multiplied_floats = tuple(map(lambda x: x * 9, tuple_floats))
print(multiplied_floats)
