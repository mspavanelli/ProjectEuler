from functools import reduce

sum = lambda a, b: a + b

def difference_between_square_of_sum_and_sum_of_squares(limit):
  numbers_list = [x for x in range(1, limit + 1)]
  squares_list = [x ** 2 for x in range(1, limit + 1) ]

  square_of_sum = reduce(sum, numbers_list) ** 2
  sum_of_squares = reduce(sum, squares_list)

  return square_of_sum - sum_of_squares

print (difference_between_square_of_sum_and_sum_of_squares(100))