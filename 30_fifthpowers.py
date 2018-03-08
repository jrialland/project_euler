from itertools import product

matchingnumbers = []

for digits in product(*[range(10) for _ in range(6)]):
    n = int(''.join(map(str,digits)))
    sum_of_powers = sum(map(lambda x:x**5, digits))
    if n > 1 and n == sum_of_powers:
        matchingnumbers.append(n)

print sum(matchingnumbers)
