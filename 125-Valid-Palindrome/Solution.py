class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re

        combinedString = (re.sub(r'[^a-zA-Z0-9]', '', s))
        lowerString = combinedString.lower()
        return (lowerString[::1] == lowerString[::-1])