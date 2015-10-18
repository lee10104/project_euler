def fibonacci(a, b, result):
  if a <= 4000000:
    if a % 2 == 0:
      result += a
      print result
    fibonacci(b, a + b, result)

fibonacci(1, 2, 0)
