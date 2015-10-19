# Problem 3: Largest prime factor

import itertools

def is_prime(num):
  if num == 1:
    return False
  for i in itertools.count(2):
    if num == i:
      break
    if num % i == 0:
      return False
  return True

def largest_prime_factor(num):
  start = int(num ** 0.5) + 1
  if start % 2 == 0:
    start -= 1
  for i in itertools.count(start, -2):
    if i == 1:
      break
    if num % i == 0:
      if is_prime(i):
        return i
  return 1

print largest_prime_factor(600851475143)
