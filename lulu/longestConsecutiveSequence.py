class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		nums_set = set(nums)
		#print(nums)
		longestConsecutiveLen = 0
		count = 0
		for num in nums_set:
			if num - 1 not in nums_set:
				current_num = num
				count = 1
				while current_num + 1 in nums_set:
					count += 1
					current_num += 1
				longestConsecutiveLen = max(longestConsecutiveLen, count)
		return longestConsecutiveLen

	def longestConsecutiveV0(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		nums.sort()
		#print(nums)
		longestConsecutiveLen = 1
		count = 1
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				continue
			elif nums[i] - nums[i-1] == 1:
				#print('count++')
				count += 1
			else:
				longestConsecutiveLen = max(longestConsecutiveLen, count)
				count = 1
				#print('--------%s' %longestConsecutiveLen)
		longestConsecutiveLen = max(longestConsecutiveLen, count)
		return longestConsecutiveLen



if __name__ == '__main__':
	mySolution = Solution()
	print(mySolution.longestConsecutive([100, 4, 200, 1, 3, 2]))
	print(mySolution.longestConsecutive([1,2,0,1]))

				
		
		
