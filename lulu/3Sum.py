class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
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
                if nums[i] + nums[left] + nums[right] == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    #print('resulsts: %s + %s + %s == 0' %(nums[i], nums[left], nums[right]))
                    while left + 1 <= len(nums) - 2:
                        if nums[left] != nums[left + 1]:
                            left += 1
                            break
                        else:
                            left += 1
                    while right - 1 >= 0:
                        if nums[right] != nums[right - 1]:
                            right -= 1
                            break
                        else:
                            right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return results


if __name__ == '__main__':
    mySolution = Solution()
    print([-1,0,1,2,-1,-4])
    print(mySolution.threeSum([-1, 0, 1, 2, -1, -4]))
    
                    
