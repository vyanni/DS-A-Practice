class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        stack = []
        hashLookup = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in hashLookup:
                stack.append(hashLookup[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True

        # bracketStack = []
        # bracketHash = {'(': ')', '[': ']', '{':'}'}

        # for bracket in s:
        #     if bracket in bracketHash:
        #         bracketStack.append(bracketHash[bracket])
        #     else:
        #         if not bracketStack:
        #             return False

        #         recent = bracketStack.pop()
        #         if recent != bracket:
        #             return False
            
        # return not bracketStack