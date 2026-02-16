class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        #Goes through each word, checks if the i-th letter is the same for each one
        for i in range(len(strs[0])):
            currentCharacter = strs[0][i]

            for words in strs[1:]:
                if i >= len(words) or words[i] != currentCharacter:
                    return strs[0][:i]
        
        return strs[0]

#Runtime: 5ms
#Memory Space: 12.46mb