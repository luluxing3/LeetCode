class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return -1
		first = 0
		last = len(nums) - 1
		i = 0
		while first <= last and i <= 10:
			i += 1
			print('first: %s \t last: %s' %(first, last))
			mid = (first + last) // 2
			print('mid: %s' %mid)
			if nums[mid] == target:
				return mid
			if nums[first] <= nums[mid]:
				#sorted before mid
				if nums[first] <= target and target < nums[mid]:
					last = mid 
				else:
					first = mid + 1
			else:
				#soryed after mid
				if nums[mid] < target and target <= nums[last]:
					first = mid + 1
				else:
					last = mid
			print('first: %s \t last: %s' %(first, last))
		return -1

	def searchVerison_0(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return -1
		if len(nums) == 1:
			return self.binarySearch(nums, 0, len(nums) -1, target)
		else:
			divide_index = self.divideNums(nums)
				
		if target >= nums[0] and target <= nums[divide_index]:
			#print('start: %s end: %s' %(0, divide_index))
			return self.binarySearch(nums, 0, divide_index, target)
		else:
			#print('start: %s end: %s' %(divide_index+1, len(nums)-1))
			return self.binarySearch(nums, divide_index+1, len(nums)-1, target)

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
