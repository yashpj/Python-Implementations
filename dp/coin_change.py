from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        # min_count = [amount+1]
        memo = {}
        def helper(i, amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            
            res = float("inf")
            for j in range(i,len(coins)):
                if amount - coins[j] >=0:
                    res = min(res, 1 + helper(j,amount-coins[j]))
            
            memo[amount] = res
            return memo[amount]
        
        min_count = helper(0, amount)
        return -1 if min_count == float("inf") else min_count
        
        