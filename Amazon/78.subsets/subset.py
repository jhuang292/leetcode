class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            size = len(ans)
            for i in range(size):
                subset = list(ans[i])
                print(subset)
                subset.append(n)
               
                ans.append(subset)
        return ans
