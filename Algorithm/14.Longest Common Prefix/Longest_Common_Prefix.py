class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs == []):
            return ""
        
        minLen = 2**31-1
        
        for i in range(len(strs)):
            if(len(strs[i]) < minLen):
                minLen = len(strs[i])
                temp = strs[i]
                

        for i in range(len(strs)):
            counter = 0
            for j in range(minLen):
                if(strs[i][j] == temp[j]):
                    counter += 1
                else:
                    break
            minLen = counter
            
        return ''.join(strs[0][:minLen])
            
