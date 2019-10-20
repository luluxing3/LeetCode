class Solution(object):
    def permutaion(self, nums):
        if len(nums) == 0:
            return [[]]
        results = []
        for index in range(len(nums)):
            rest_results = self.permutaion(nums[: index] + nums[index + 1 :])
            for rest in rest_results:
                per = [nums[index]]
                per.extend(rest)
                results.append(per)
        return results


if __name__ == '__main__':
    nums = [1,2,3]
    mySolution = Solution()
    print(mySolution.permutaion(nums))
