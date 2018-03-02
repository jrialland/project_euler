
_primes=set([])
def is_prime(n):
  if n in _primes: return True
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  _primes.add(n)
  return True

def count_quadprimes(a, b):
    n = 1
    while is_prime(n**2 + a * n + b):
       n+=1
    return n

#----------------
maxprimes = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        c = count_quadprimes(a, b)
        if c > maxprimes:
            maxprimes = c
            solution = a * b
print solution

