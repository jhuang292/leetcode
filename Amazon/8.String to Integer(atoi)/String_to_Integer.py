import re
matcher = re.compile(r'^ *([-\+]?\d+)')

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        match = matcher.match(str)

        if not match:
            return 0
        else:
            num = int(match.group(1))
            
            if num > 0:
                return min(num, 2**31 - 1)
            elif num < 0:
                return max(num, -2**31)
            else:
                return 0
