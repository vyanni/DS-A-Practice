class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def topDown(i, j):
            if j == len(p):
                return i == len(s)
            
            match = j < len(p) and (p[j] == s[i] or p[j] == '.')
            #if 


        # memo = {}

        # def dp(currentS, currentP):
        #     if (currentS, currentP) in memo:
        #         return memo[(currentS, currentP)]

        #     if currentP == len(p):
        #         return currentS == len(s)
            
        #     currentMatch = currentS < len(s) and (s[currentS] == p[currentP] or p[currentP] == '.')
        #     if (currentP + 1) < len(p) and p[currentP + 1] == '*':
        #         memo[(currentS, currentP)] = dp(currentS, currentP+2) or (currentMatch and dp(currentS + 1, currentP))
        #     else:
        #         memo[(currentS, currentP)] = currentMatch and dp(currentS+1, currentP+1)

        #     return memo[(currentS, currentP)]

        # return dp(0, 0)