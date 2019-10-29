class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = 0
        while i <= reach and i <= len(nums) - 1:
            reach = max(reach, nums[i] + i)
            i += 1
        return reach >= len(nums) - 1

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        return self.dp(nums)[0]

    def dp(self, nums):
        ans = [None] * len(nums)
        ans[-1] = True
        distance = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= distance:
                ans[i] = True
                distance = 1
            else:
                ans[i] = False
                distance += 1
        return ans 

