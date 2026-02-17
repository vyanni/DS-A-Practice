class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        fixedElement = nums[0]

        for i in range(len(nums) - 2):
            leftPointer = 1
            rightPointer = len(nums) - 1

            if(nums[leftPointer] + nums[rightPointer])