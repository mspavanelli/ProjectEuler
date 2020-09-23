from functools import reduce

sum = lambda a, b: int(a) + int(b)

def sum_of_digits(n):
  return int(reduce(sum, list(str(n))))

list = [sum_of_digits(a ** b) for a in range(100) for b in range(100)]

max_value = max(list)

print (max_value)