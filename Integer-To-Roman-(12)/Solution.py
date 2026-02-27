class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        legendArray = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        romanNumeral = ''
        for value in sorted(legendArray.keys(), reverse = True):
            while num >= value:
                if (num - value) >= 0:
                    romanNumeral += legendArray[value]
                    num -= value
        
        return romanNumeral