class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0] * (n + 1)
        ans[0] = 1
        ans[1] = 1
        for i in range(2, n + 1):
            for k in range(1, i + 1):
                ans[i] += ans[i - k] * ans[k - 1]
        return ans[-1]
