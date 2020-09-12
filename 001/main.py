from functools import reduce

LIMIT = 1000

def is_multiple_of_3_or_5(n):
  is_multiple_of_3 = n % 3 == 0
  is_multiple_of_5 = n % 5 == 0

  return is_multiple_of_3 or is_multiple_of_5

list = [x for x in range(LIMIT) if is_multiple_of_3_or_5(x)]

sum = lambda a, b: a + b

total = reduce(sum, list)

print (total)