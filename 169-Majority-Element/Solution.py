class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashTable = {}

        for num in nums:
            if num not in hashTable:
                hashTable[num] = 0
            
            hashTable[num] += 1
            if hashTable[num] > (len(nums) // 2):
                return num
        
        