class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) -1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        #reverse after i+1 
        start = i + 1
        end = len(nums) -1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

            
        

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.nextPermutation([1, 2, 3]))
    print(mySolution.nextPermutation([3, 2, 1]))
    print(mySolution.nextPermutation([1, 1, 5]))
    print(mySolution.nextPermutation([1, 3, 2]))

