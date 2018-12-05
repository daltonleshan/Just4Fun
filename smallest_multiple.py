def smallestMultiple(n):
    divisors = list(range(1, n + 1))
    for i in range(n, 9999999999, n):
        if all(i % j == 0 for j in divisors):
            return i
    return None

print(smallestMultiple(10))
print(smallestMultiple(20))
