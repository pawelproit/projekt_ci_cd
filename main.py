def multiply(n, m):
  return n * m

def silnia(n):
  if n > 1:
    return multiply(n, silnia(n - 1))
  return 1
