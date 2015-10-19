# Problem 6: Sum square difference

def sum_of_squares(num):
  result = 0
  for i in range(num):
    result += (i + 1) * (i + 1)
  return result

def square_of_sum(num):
  result = 0
  for i in range(num):
    result += i + 1
  return result * result

print square_of_sum(100) - sum_of_squares(100)
