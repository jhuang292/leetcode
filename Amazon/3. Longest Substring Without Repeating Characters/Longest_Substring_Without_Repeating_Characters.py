class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp, max_v, j = {}, 0, -1
        
        for i, c in enumerate(s):
            if c in dp: 
                j = max(j, dp[c])
            
            dp[c], max_v = i, max(max_v, i-j)
        return max_v
                    
        
