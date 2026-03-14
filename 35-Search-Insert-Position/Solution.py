class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        leftPointer = 0
        rightPointer = len(nums)

        while leftPointer < rightPointer:
            midPoint = (leftPointer + rightPointer) // 2
            if nums[midPoint] < target:
                leftPointer = midPoint + 1
            else:
                rightPointer = midPoint

        return leftPointer