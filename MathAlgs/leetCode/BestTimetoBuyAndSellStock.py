def maxProfit(prices):
    if len(prices) == 0:
        return 0

    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            maxP = max(maxP, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return maxP

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # 5