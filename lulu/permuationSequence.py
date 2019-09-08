import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numset = [i for i in range(1, n+1)]
        retnum = []
        k = k - 1
        while len(numset) > 1:
            n = n - 1
            index = k / math.factorial(n)
            retnum.append(str(numset[index]))
            k = k % math.factorial(n)
            numset.remove(numset[index])
        retnum.append(str(numset[0]))
        return ''.join(retnum)


    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return self.factorial(n - 1) * n

    def getPermutationV0(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        m = 1
        factorial_m = 1
        #if k == 1:
        #    return ''.join([str(x) for x in range(1, n + 1)])
        while k > factorial_m * (m + 1):
            m += 1
            factorial_m = factorial_m * m
        nums = range(1, n-m+1) + range(n, n-m, -1)
        #print('m=%s' %m)
        #print('factorial_m=%s' %factorial_m)
        #print(nums)

        for i in range(k - factorial_m):
            #print('next')
            self.nextPermutation(nums)
        #print(nums)
        return ''.join([str(x) for x in nums])

		 
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
  
if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.getPermutation(3, 3))
    print(mySolution.getPermutation(2, 2))
