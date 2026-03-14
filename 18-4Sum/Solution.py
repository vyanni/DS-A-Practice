class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        setList = []

        for i in range(len(nums) - 3):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums) - 2):

                if j > (i+1) and nums[j] == nums[j-1]:
                    continue

                leftPointer = j + 1
                rightPointer = len(nums) - 1

                while leftPointer < rightPointer:
                    totalSum = nums[i] + nums[j] + nums[leftPointer] + nums[rightPointer]

                    if totalSum == target:
                        setList.append([nums[i], nums[j], nums[leftPointer], nums[rightPointer]])

                        while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer + 1]:
                            leftPointer += 1
                        while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer - 1]:
                            rightPointer -= 1

                        leftPointer += 1
                        rightPointer -= 1
                    
                    elif totalSum < target:
                        leftPointer += 1
                    else:
                        rightPointer -= 1
        
        return setList
    
#Runtime: 771ms 
# {O(n^2) -> Takes O{n log n} to sort, then O(n) to fix each element, then O(n) to move the pointers per fixed element
# This results in O(n^2) for the main look-through loop, and combined, its O(n logn + n^2), where n^2 grows faster so overall its
# O(n^2)}
#Memory Space: 18.98mb 
#{For sorting, it takes O(log n) space, and returning there can be at most a possible of O(n^2) triplets}