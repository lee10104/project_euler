# Problem 4: Largest palindrome product

def is_palindrome(num):
  string = str(num)
  length = len(string)
  for i in range(length / 2):
    if string[i] != string[length - i - 1]:
      return False
  return True

palindromelist = []
for i in range(100, 1000):
  for j in range(100, 1000):
    if is_palindrome(i * j):
      palindromelist.append(i * j)

palindromelist.sort()
palindromelist.reverse()

print palindromelist[0]
