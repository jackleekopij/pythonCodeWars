#### Script to print out Fibonacci numbers.

def fibonacciValues(n):
  fibonacci_value = 2
  immediate_previous = 1
  second_previous = 1
  if n  == 0 or n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    for i in range(2,n):
      fibonacci_value = immediate_previous + second_previous
      print("The immediate_previous was: " + str(immediate_previous))
      print("The second previous was: " + str(second_previous))
      print("The fibonaccie value was: " + str(fibonacci_value))
      second_previous = immediate_previous
      immediate_previous = fibonacci_value
  return fibonacci_value

print(fibonacciValues(8))
