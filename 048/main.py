from functools import reduce

serie = [x ** x for x in range(1, 1001)]

sum = lambda a, b: a + b

total = reduce(sum, serie)

last_ten_digits_of_sum = str(total)[-10:]

print (last_ten_digits_of_sum)