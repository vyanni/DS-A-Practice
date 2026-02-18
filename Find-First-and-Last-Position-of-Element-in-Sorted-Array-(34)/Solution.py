class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        leftPointer = 0
        rightPointer = len(nums)
        targetBounds = []

        while(leftPointer < rightPointer):
            midPoint = (leftPointer + rightPointer) // 2

            if nums[midPoint] < target:
                leftPointer = midPoint + 1
            else:
                rightPointer = midPoint

        targetBounds.append(leftPointer)
        
        leftPointer = 0
        rightPointer = len(nums)

        while(leftPointer < rightPointer):
            midPoint = (leftPointer + rightPointer) // 2

            if nums[midPoint] < (target + 1):
                leftPointer = midPoint + 1
            else:
                rightPointer = midPoint
        
        targetBounds.append(leftPointer - 1)

        if targetBounds[0] < len(nums) and nums[targetBounds[0]] == target:
            return targetBounds
        else:
            return [-1, -1]