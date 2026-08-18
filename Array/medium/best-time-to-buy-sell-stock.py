# Best time to buy and sell stock 
# [7,1,5,3,6,4] -> max profit -> 5 


def maxProfit(prices:list[int]):
    min = prices[0]
    profit = 0 
    n = len(prices)
    for i in range(1,n):
        cost = prices[i] - min 
        profit = max(profit, cost) 
        if min > prices[i]:
            min = prices[i] 
    return profit

print(maxProfit([7,1,5,3,6,4]))
