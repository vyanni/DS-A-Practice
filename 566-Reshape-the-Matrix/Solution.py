class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        if (r * c) != (m * n) or (r == m and c == n):
            return mat
        
        newMat = [[0 for i in range(c)] for i in range(r)]
        for i in range(m*n):
            newMat[i // c][i % c] = mat[i // n][i % n]

        return newMat