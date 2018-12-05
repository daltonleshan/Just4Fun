import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def summationOfPrimes(limit):
    if limit is None:
        return 0
    return sum([j for j in range(0, limit + 1) if isPrime(j)])

print(summationOfPrimes(10))
print(summationOfPrimes(2000000))
