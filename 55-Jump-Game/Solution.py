class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        if goal == 0:
            return True
        return False

        # memo = {}

        # def topDown(index):
        #     if index >= len(nums) - 1:
        #         return True
            
        #     if index in memo:
        #         return memo[index]
            
        #     if nums[index] == 0:
        #         memo[index] = False
        #         return False
        
        #     for i in range(nums[index], 0, -1):
        #         if topDown(index + i):
        #             memo[index] = True
        #             return True
            
        #     memo[index] = False
        #     return memo[index]
        
        # return topDown(0)

        
        