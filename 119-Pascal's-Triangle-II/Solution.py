class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        currentRow = [1]
        for i in range(rowIndex):
            currentRow = [leftSide + rightSide for leftSide, rightSide in zip([0] + currentRow, currentRow + [0])]
        
        return currentRow