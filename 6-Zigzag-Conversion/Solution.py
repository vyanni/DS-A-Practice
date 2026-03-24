class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        zigzag = ''
        spread = (2*(numRows-1))
        
        for i in range(numRows):
            for leftPointer in range(i, len(s), spread):
                zigzag += s[leftPointer]
                if i and (leftPointer + (spread - (2*i))) < len(s) and (2*i) != spread:
                    zigzag += s[leftPointer + (spread - (2*i))]
        
        return zigzag

