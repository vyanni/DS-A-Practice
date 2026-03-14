class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        charHash = {}
        leftPointer = 0
        maxLength = 0

        for rightPointer in range(len(s)):
            currentChar = s[rightPointer]

            if(currentChar in charHash and charHash[currentChar] >= leftPointer):
                leftPointer = charHash[currentChar] + 1
            
            charHash[currentChar] = rightPointer
            maxLength = max(maxLength, rightPointer - leftPointer +1)
        
        return maxLength