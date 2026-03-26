class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {len(s) : True}

        def backtracking(index):
            if index in memo:
                return memo[index]
            
            for word in wordDict:
                if (index + len(word)) <= len(s) and s[index:index+len(word)] == word:
                    if backtracking(index + len(word)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False
        
        return backtracking(0)

        # def backtracking(currentWord):
        #     if currentWord == s:
        #         return True
            
        #     if len(currentWord) > len(s):
        #         return None
            
        #     for i in range(len(wordDict)):
        #         true = backtracking(currentWord + wordDict[i]) 
        #         if true:
        #             return True
        #     return False
        
        # return backtracking('')
        