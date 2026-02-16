class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #The idea is to have 2 points for each ends of the array, and move the pointer with the less height
        leftPointer = 0
        rightPointer = len(height) - 1
        maxArea = 0

        while leftPointer < rightPointer:
            boxWidth = rightPointer - leftPointer
            boxHeight = min(height[rightPointer], height[leftPointer])
            currentArea = (boxHeight * boxWidth)
            maxArea = max(currentArea, maxArea)

            if(height[rightPointer] < height[leftPointer]):
                rightPointer -= 1
            else:
                leftPointer += 1
        
        return maxArea

