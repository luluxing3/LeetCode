class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return False
		if len(nums) == 1:
			if self.binarySearch(nums, 0, len(nums) -1, target) != -1:
				return True
			else:
				return False
		else:
			divide_index = self.divideNums(nums)
				
		if target >= nums[0] and target <= nums[divide_index]:
			#print('start: %s end: %s' %(0, divide_index))
			if self.binarySearch(nums, 0, divide_index, target) != -1:
				return True
			else:
				return False
		else:
			#print('start: %s end: %s' %(divide_index+1, len(nums)-1))
			if self.binarySearch(nums, divide_index+1, len(nums)-1, target) != -1:
				return True
			else:
				return False

	def binarySearch(self, nums, start_index, end_index, target):
		if start_index > end_index:
			return -1
		mid_index = (end_index + start_index) // 2
		if target == nums[mid_index]:
			return mid_index
		elif target < nums[mid_index]:
			return self.binarySearch(nums, start_index, mid_index -1, target)
		else:
			return self.binarySearch(nums, mid_index + 1, end_index, target)  

	def divideNums(self, nums):
		ascending_count = 0
		for index in range(len(nums)-1):
			if nums[index] <= nums[index + 1]:
				ascending_count += 1
			else:
				break
		return ascending_count
