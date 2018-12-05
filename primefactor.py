import math

def largestPrimeFactor(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            factors.add(i)
    if n > 2:
        factors.add(n)
    return max(factors)

print(largestPrimeFactor(25))
print(largestPrimeFactor(101))
print(largestPrimeFactor(600851475143))

