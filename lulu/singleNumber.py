class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for x in nums:
            result = result ^ x

        return result


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.singleNumber([1,1,2,3,3]))
