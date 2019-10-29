class Solution(object):
    def maximum(self, nums):
        maxSum = -float('inf')
        currSum = 0
        for i in range(len(nums)):
            maxSum = max(maxSum, currSum + nums[i])
            currSum = max(0, nums[i], currSum + nums[i])
        return maxSum

    def maximumV1(self, nums):
        ans = [None] * len(nums)
        ans[-1] = nums[-1]
        largestSum = ans[-1]
        for i in range(len(nums) - 2, -1, -1):
            ans[i] = max(nums[i], nums[i] + ans[i + 1])
            largestSum = max(ans[i], largestSum)
        return largestSum

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.maximum([-2, 1, -3, 4, -1, 2, 1, -5, -4]))
            
            
