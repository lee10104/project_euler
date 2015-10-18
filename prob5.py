def is_prime(num):
  if num == 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def factorize(num, end):
  result = {}
  for i in range(2, end + 1):
    if is_prime(i):
      temp = num
      n = 0
      while temp % i == 0:
        n += 1
        temp /= i
      result[i] = n
  return result

result = []
answer = 1

for i in range(1, 21):
  result.append(factorize(i, 20))

for i in range(1, 21):
  largest = 0
  if is_prime(i):
    for j in range(20):
      if largest < result[j][i]:
        largest = result[j][i]
  answer *= i ** largest

print answer
