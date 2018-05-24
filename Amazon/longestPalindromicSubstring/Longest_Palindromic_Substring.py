class Solution:
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        
        for i in range(len(s)):
            
            length1 = self.findLong(s, i, i)
            length2 = self.findLong(s, i, i+1)
            maxLen = max(length1, length2)
            
            if(maxLen > end - start):
                
                start = i - int((maxLen-1)/2)
                end = i + int(maxLen/2)
                
        return s[start:end+1]
            
    def findLong(self,s, L, R):
        
        while(L >= 0 and R <= len(s) -1 and s[L] == s[R]):
            
            L -= 1
            R += 1
            
        return R - L - 1   
