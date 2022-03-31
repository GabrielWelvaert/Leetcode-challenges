def maxProfit(prices):
    minp = prices[0]
    maxp = 0
    for p in prices:
        if p < minp:
            minp = p
        elif p - minp > maxp:
            maxp = p - minp
    return maxp

