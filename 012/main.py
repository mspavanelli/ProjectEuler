def triangle_number(n):
  if n == 0:
    return 0
  
  return n + triangle_number(n - 1)

print (triangle_number(1))
print (triangle_number(2))
print (triangle_number(3))
print (triangle_number(4))
print (triangle_number(5))
print (triangle_number(6))
print (triangle_number(7))
