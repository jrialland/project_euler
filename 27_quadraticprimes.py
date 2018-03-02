
from utils import is_prime

def count_quadprimes(a, b):
    n = 1
    while is_prime(n**2 + a * n + b):
       n+=1
    return n

m, sa, sb = 0, 0, 0
for a in range(-999,1000):
    for b in range(-999, 1000):
       c = count_quadprimes(a,b)
       if c > m:
           m = c
           sa, sb = a, b
print sa * sb

