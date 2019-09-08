class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i <= len(nums)-1:
            if nums[i] == val:
                nums[i] = nums[-1]
                nums.pop()
            else:
                i += 1
        return i
        
    def removeElementV0(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j and i <= len(nums) -1 and j >= 0:
            while i < j and i <= len(nums) -1 and nums[i] != val:
                i += 1
            while i < j and j >= 0 and nums[j] == val:
                j -= 1
            if i <= len(nums) -1 and j >= 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
         
        count = 0
        for x in nums:
            if x != val:
                count += 1
            else:
                break

        return count


if __name__ == '__main__':
    mySolution = Solution()
    #print(mySolution.removeElementV0([3,2,2,3], 3))
    #print(mySolution.removeElementV0([3,3], 3))
    print(mySolution.removeElementV0([4,5], 5))
    print(mySolution.removeElementV0([4,5], 4))


