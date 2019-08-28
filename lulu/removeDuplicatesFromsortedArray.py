class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
        	return len(nums)

        i = 0
        for j in range(1, len(nums)):
        	if nums[j] == nums[i]:
        		pass
        	else:
        		i += 1
        		nums[i] = nums[j]
        return i+1
