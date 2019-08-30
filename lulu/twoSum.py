class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for index, x in enumerate(nums):
            #print(hash_dict)
            if x in hash_dict:
                return [hash_dict[x], index]
            else:
                hash_dict[target - x] = index


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    mySolution = Solution()
    print(mySolution.twoSum(nums, target))

            
                

        
