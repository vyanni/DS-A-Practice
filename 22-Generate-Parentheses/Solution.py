class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        parenthesesPath = []

        def backtracking(currentPath, openNum, closedNum):
            if len(currentPath) == (2*n):
                parenthesesPath.append(currentPath)
            
            if openNum < n:
                backtracking(currentPath + '(', openNum + 1, closedNum)

            if closedNum < openNum:
                backtracking(currentPath + ')', openNum, closedNum + 1)

        backtracking('', 0, 0)
        return parenthesesPath 

        