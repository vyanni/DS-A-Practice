class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        squareTriples = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                for q in range(j, n+1):
                    if ((i*i) + (j*j) == (q*q)):
                        squareTriples += 2
        
        return squareTriples