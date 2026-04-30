class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
        def isPrime(num):
            if num < 2:
                return False
            elif num == 2:
                return True
            elif not num % 2:
                return False
            for i in range(3, int(sqrt(num))+1, 2):
                if not num % i:
                    return False
            return True
        
        greatestPrime = 0
        for i in range(len(nums)):
            currentNum = nums[i][i]
            if isPrime(currentNum):
                greatestPrime = max(greatestPrime, currentNum)
            
        for i in range(len(nums)):
            currentNum = nums[i][len(nums) - i - 1]
            if isPrime(currentNum):
                greatestPrime = max(greatestPrime, currentNum)
        
        return greatestPrime
            