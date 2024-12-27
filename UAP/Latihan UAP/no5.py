from functools import reduce

odd_numbers = [x for x in range(1, 100, 2)]
multiples_of_9 = list(filter(lambda x: x % 9 == 0, odd_numbers))

first_five_multiples = multiples_of_9[:5]
product_of_first_five = reduce(lambda x, y: x * y, first_five_multiples)
print(product_of_first_five)
