class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        lowestDifference = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            leftPointer = i + 1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                totalSum = nums[i] + nums[leftPointer] + nums[rightPointer]
                currentDifference = abs(totalSum - target)

                if currentDifference < abs(lowestDifference - target):
                    lowestDifference = totalSum

                if totalSum < target:
                    leftPointer += 1
                elif totalSum > target:
                    rightPointer -= 1
                else:
                    return totalSum
        
        return lowestDifference