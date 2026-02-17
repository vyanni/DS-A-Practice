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

        #Calculate area, consistently move in pointers depending on their height
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

#Runtime 127ms { O(n) -> Worst case scenario, you have to check each and every element}
#Space: 20.75mb { O(1) - > Worst case scenario uses the same amount of memory each time (The 2 pointers, max and current area)}