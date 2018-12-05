def sumEvenFib(limit):
    e1 = 0
    e2 = 2
    sum = 0
    while e2 < limit:
        sum += e2
        e3 = 4 * e2 + e1
        e1 = e2
        e2 = e3

    return sum

print(sumEvenFib(34))
print(sumEvenFib(4000000))
