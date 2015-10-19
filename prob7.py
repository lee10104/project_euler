# Problem 7: 10001st prime

import itertools

def is_prime(num):
  if num != 2 and num % 2 == 0:
    return False
  if num != 3 and num % 3 == 0:
    return False
  if num != 5 and num % 5 == 0:
    return False
  if num != 7 and num % 7 == 0:
    return False
  for i in range(11, num):
    if num % i == 0:
      return False
  if num == 1:
    return False
  return True

def nst_prime(n):
  flag = 0
  for i in itertools.count(2):
    if is_prime(i):
      flag += 1
      if flag == n:
        return i

print nst_prime(10001)
