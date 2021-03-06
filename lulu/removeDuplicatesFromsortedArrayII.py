class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
        	return len(nums)
        i = 0
        duplicate_count = 1
        for j in range(1, len(nums)):
        	if nums[j] == nums[i]:
        		duplicate_count += 1
        		if duplicate_count <= 2:
        			i += 1
        			nums[i] = nums[j]
        	if nums[j] != nums[i]:
        		duplicate_count = 1
        		i += 1
        		nums[i] = nums[j]
        return i + 1
