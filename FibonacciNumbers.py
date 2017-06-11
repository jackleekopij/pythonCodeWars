#### Script to print out Fibonacci numbers.

def fibonacciValues(n):
  if n  == 0: return 0
  elif n == 1: return 1
  else: return fibonacciValues(n-1) + fibonacciValues(n-2)

print(fibonacciValues(8))
