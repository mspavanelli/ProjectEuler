from functools import reduce

LIMIT = 10

def is_even(n):
  return n % 2 == 0

fibonacci_numbers = [1, 2]

while True:
  next_value = fibonacci_numbers[-1] + fibonacci_numbers[-2]

  if next_value > 4000000:
    break

  fibonacci_numbers.append(next_value)

even_valued_terms = filter(is_even, fibonacci_numbers)

sum = lambda a, b: a + b

total = reduce(sum, even_valued_terms)

print(total)