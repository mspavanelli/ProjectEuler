def is_palindrome(n):
  return str(n) == str(n)[::-1]

list_of_palindromes = [(x * y) for x in range(100, 1000) for y in range(100, 1000) if is_palindrome(x * y)]

max_value = max(list_of_palindromes)

print (max_value)
