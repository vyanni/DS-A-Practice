class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}

        def topDown(remainder):
            if remainder == 0:
                return 0
            
            if remainder < 0:
                return float('inf')
            
            if remainder in memo:
                return memo[remainder]

            minCoins = float('inf')
            for coin in coins:
                minCoins = min(minCoins, topDown(remainder - coin) + 1)
            
            memo[remainder] = minCoins
            return minCoins
        
        result = topDown(amount)
        return result if result != float('inf') else -1

        # dp = [float('inf')] * (amount + 1)

        # dp[0] = 0

        # for i in range(1, amount+1):
        #     for coin in coins:
        #         if i-coin >= 0:
        #             dp[i] = min(dp[i], dp[i-coin] + 1)
        
        # return dp[amount] if dp[amount] != float('inf') else -1

        # memo = {}

        # def dfs(remainder):
        #     if remainder == 0:
        #         return 0
            
        #     if remainder < 0:
        #         return float('inf')
            
        #     if remainder in memo:
        #         return memo[remainder]
            
        #     currentAnswer = float('inf')

        #     for coin in coins:
        #         currentAnswer = min(currentAnswer, dfs(remainder - coin) + 1)
            
        #     memo[remainder] = currentAnswer
        #     return currentAnswer
        
        # result = dfs(amount)
        # return result if result != float('inf') else -1

        # if amount == 0:
        #     return 0
        
        # heap = []

        # def backtracking(currentSum, numCoins, currentIndex):
        #     if currentSum == amount:
        #         heapq.heappush(heap, numCoins)
        #         return
            
        #     if currentSum > amount:
        #         return

        #     print(amount)
        #     for i in range(currentIndex, -1, -1):
        #         backtracking(currentSum + coins[i], numCoins + 1, i)
        
        # backtracking(0, 0, len(coins) - 1)

        # if heap:
        #     return heapq.heappop(heap)
        # else:
        #     return -1


