def max_profit(prices: list):
    profit = 0
    for i in range(len(prices)):
        if prices[i] < prices[i+1]:
            profit += prices[i+1]-prices[i]
    return profit


prices = [7,6,4,3,1]
print(max_profit(prices))



