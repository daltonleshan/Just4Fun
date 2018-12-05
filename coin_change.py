def count(coin_den, val):
    num_ways = [0 for i in range(val + 1)]
    num_ways[0] = 1
    for coin in coin_den:
        for value in range(coin, val + 1):
            num_ways[value] += num_ways[value - coin]
    return num_ways[val]

print(count([1,2,5], 10))
print(count([1,2,3], 4))
print(count([1,2,5], 15))
print(count([1,2,5,10,20,50,100,200], 200))
