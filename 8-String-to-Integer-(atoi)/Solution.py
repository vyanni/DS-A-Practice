class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringNum = ''
        s = s.strip()
        if not s:
            return 0

        sign = 0
        if s[0] == '-':
            sign = -1
        elif s[0] == '+':
            sign = 1

        for i, char in enumerate(s):
            if sign and i == 0:
                continue

            if char.isdigit():
                stringNum += char
            else:
                break
        
        if not sign:
            sign = 1

        if stringNum: 
            stringNum = (int(stringNum)) * sign
        else:
            return 0

        if stringNum <= 2147483647 and stringNum >= -2147483648:
            return stringNum
        elif stringNum > 2147483647:
            return 2147483647
        elif stringNum < -2147483648:
            return -2147483648