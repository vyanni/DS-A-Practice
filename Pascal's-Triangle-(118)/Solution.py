class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        pascalTriangle = [[1]]
        for i in range(numRows - 1):
            lastRow = pascalTriangle[-1]
            currentRow = [1]

            for j in range(1, i+1):
                currentRow.append(lastRow[j-1] + lastRow[j])

            pascalTriangle.append(currentRow + [1])
        
        return pascalTriangle

