class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        matrix[:] = [list(row[::-1]) for row in zip(*matrix)]

        # matrix[:] = [list(row[::-1]) for row in zip(*matrix)]