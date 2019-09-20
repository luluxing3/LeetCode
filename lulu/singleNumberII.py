class Solution(object):
    def singleNumber(self, nums):
        t1 = 0
        t2 = 0
        t3 = 0

        for x in nums:
            t2 = t2 | (t1 & x) #occur twice
            t1 = t1 ^ x #occur once
            t3 = t1 & t2 #occur three times

            t1 = t1 & (~t3) #turn to zero if occur three times
            t2 = t2 & (~t3) #turn to zero if occur three times
        return t1


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.singleNumber([3,1,1,2,1,3,3]))
