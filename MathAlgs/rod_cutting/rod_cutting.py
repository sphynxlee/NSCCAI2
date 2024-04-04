def rod_cutting(length, prices):
    n = len(prices)
    # initialize the revenue array to store the maximum revenue for each length
    revenue = [0] * (length + 1)

    for i in range(1, length + 1):
        max_val = float('-inf')
        for j in range(1, min(i, n) + 1):
            max_val = max(max_val, prices[j - 1] + revenue[i - j])
        revenue[i] = max_val

    return revenue[length]

prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
max_revenue = rod_cutting(rod_length, prices)
print("the length is:", rod_length, ", and the maximum revenue is:", max_revenue)