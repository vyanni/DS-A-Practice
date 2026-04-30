class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        newMatrix = [[0 for i in range(n)] for i in range(n)]
        left, top = 0, 0
        right, bottom = n - 1, n - 1
        count = 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                newMatrix[top][i] = count
                count += 1
            top += 1

            for i in range(top, bottom + 1):
                newMatrix[i][right] = count
                count += 1
            right -= 1

            for i in range(right, left - 1, -1):
                newMatrix[bottom][i] = count
                count += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                newMatrix[i][left] = count
                count += 1
            left += 1
        
        return newMatrix


        # newMatrix = [[] for i in range(n)]
        # for i in range(1, n):
        #     newMatrix[0].append(i)

        # for i in range(3*n - 2, 2*n - 2, -1):
        #     newMatrix[-1].append(i)
        
        # innerRows = n-1
        # while innerRows >= 2:
        #     for i in range(4*n - 4, 4*n - 4 + innerRows):
        #         newMatrix[n - innerRows].append(i)
        #     newMatrix[n - innerRows].append(newMatrix[n - innerRows - 1][-1] + 1)
        #     innerRows -= 1

        #     for i in range()


