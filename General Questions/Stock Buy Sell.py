"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

print("Enter the list of price of stocks separated by spaces:")
prices = list(map(int, input().split()))

"""
Brute Force Approach
n = len(prices)
ans = 0
for i in range(n):
    for j in range(i, n):
        ans = max(ans, prices[j] - prices[i])

print(ans)
"""

# Two Pointers

n = len(prices)

buy = 0 # start the buy pointer from index 0 
sell = 1 # start the sell pointer from index 1

max_profit = 0 

while sell < n:
    if prices[buy] < prices[sell]: # until the price at the assumed selling day is more than the assumed buy day
        profit = prices[sell] - prices[buy]
        max_profit = max(max_profit, profit) # If new max profit found, store it
        
    else: #when the loss starts, we change the buy day and start the process again. 
        buy = sell
    
    sell += 1

print(max_profit)