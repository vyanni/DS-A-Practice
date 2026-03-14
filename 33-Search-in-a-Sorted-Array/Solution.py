class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:

            midPoint = (leftPointer + rightPointer) // 2
            if nums[midPoint] == target:
                return midPoint

            if nums[leftPointer] <= nums[midPoint]:
                 if nums[leftPointer] <= target < nums[midPoint]:
                    rightPointer = midPoint - 1
                 else:
                    leftPointer = midPoint + 1
            else:
                if nums[midPoint] < target <= nums[rightPointer]:
                    leftPointer = midPoint + 1
                else:
                    rightPointer = midPoint - 1
        
        return -1