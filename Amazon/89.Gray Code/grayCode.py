class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        solution = [0]
        for i in range(n):
            for num in reversed(solution):
                solution.append(2**(i)+num)
        return solution

