class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        m = len(mat)
        n = len(mat[0])
        diagonal = []

        for i in range(m*n):
            if i % 2:
                for j in range(i+1):
                    if j < m and (i-j) < n:
                        diagonal.append(mat[j][i-j])
            else:
                for j in range(i+1):
                    if (i-j) < m and j < n:
                        diagonal.append(mat[i-j][j])
        
        return diagonal