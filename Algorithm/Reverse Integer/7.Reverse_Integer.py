class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rList = []
        start = 0
        
        
        x = str(x)
        end = len(x)-1
        if(x[0] == '-'):
            start = 1
            rList.append(x[0])
            while(end != start-1):
                rList.append(x[end])
                end -= 1
        else:
            while(end != start-1):
                rList.append(x[end])
                end -= 1
                
        if(int(''.join(rList)) < -2**31 or int(''.join(rList)) > 2**31-1):
            return 0
        return int(''.join(rList))
        
