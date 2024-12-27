odd_numbers = [x for x in range(1, 100, 2)]

multiples_of_9 = list(filter(lambda x: x % 9 == 0, odd_numbers))
print(multiples_of_9)
