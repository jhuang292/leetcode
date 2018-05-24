class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        index = 0
        
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if(nums[i] + nums[i+1+j] == target):
                    return [i, i+1+j]
        
