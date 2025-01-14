def multiply(n, m):
  return n * m

def factorial(n):
  if n > 1:
    return multiply(n, factorial(n - 1))
  return 1
