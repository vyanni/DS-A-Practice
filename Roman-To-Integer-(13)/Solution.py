class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanArray = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1 
        }

        integerSum = 0
        previousNum = 0

        for character in s[::-1]:
            currentNum = romanArray[character]
            if currentNum < previousNum:
                integerSum -= currentNum
            else:
                integerSum += currentNum
            previousNum = currentNum

        return integerSum
            