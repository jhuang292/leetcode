class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if(x[0] == '-'):
            return False
        start = 0
        end = len(x)-1

            
        while(end != start):
            if(x[end] == x[start]):
                if(end == start + 1):
                    return True
                else:
                    end -= 1
                    start += 1
            else:
                return False
        return True
            
