# max transactions allowed is 2

def maxProfit(stocks):
    n = len(stocks)
    profit = [0 for _ in range(n)]
    max_p = stocks[n - 1]
    for i in range(n-2, 0, -1):
        max_p = max(max_p, stocks[i])
        profit[i] = max(profit[i+1], max_p - stocks[i])
    min_p = stocks[0]
    for i in range(1, n):
        min_p = min(min_p, stocks[i])
        profit[i] = max(profit[i-1], profit[i] + stocks[i] - min_p)
    return profit[n-1]

print(maxProfit([10,22,5,75,65,80]))
