class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        setBits = 0
        while n:
            setBits += (n&1)
            n = n >> 1
        
        return setBits