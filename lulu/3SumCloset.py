class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float("inf")
        results = None
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            #print('------i=%s-----' %i)
            if i - 1 >= 0:
                if nums[i] == nums[i-1]:
                    continue
            while left < right:
                #print('left=%s\tright=%s' %(left, right))
                if abs(target - (nums[i] + nums[left] + nums[right])) < diff:
                    results = nums[i] + nums[left] + nums[right]
                    diff = abs(target - (nums[i] + nums[left] + nums[right]))
                    #print('resulsts: %s + %s + %s \t diff=%s' %(nums[i], nums[left], nums[right], diff))
                if nums[i] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return results


if __name__ == '__main__':
    mySolution = Solution()
    #print([-1,0,1,2,-1,-4])
    #print(mySolution.threeSumClosest([-1, 0, 1, 2, -1, -4], 3.5))

    print([0,2,1,-3])
    print(mySolution.threeSumClosest([0, 2, 1, -3], 1))
    print("="*20)


    print([1,1,-1,-1,3])
    print(mySolution.threeSumClosest([1,1,-1,-1,3], 3))

    
                    
