#class Solution(object):
#    def subsets(self, nums):
#        results = [[]]
#        nums.sort()
#        for n in nums:
#            for subset in results[:]:
#                newSubset = subset[:]
#                newSubset.append(n)
#                results.append(newSubset)
#        return results
#
#class Solution(object):
#    def __init__(self):
#        self.ans = []
#
#    def subsets(self, nums):
#        def dfs(path, level):
#            if level == len(nums):
#                self.ans.append(path[:])
#            else:
#                dfs(path, level + 1)
#
#                path = path[:]
#                path.append(nums[level])
#                dfs(path, level + 1)
#
#        nums.sort()
#        dfs([], 0)
#        return self.ans
 

class Solution(object):
    def subsets(self, nums):
        def k2sub(k):
            sub = []
            for index in range(len(nums)):
                if k & 1:
                    sub.append(nums[index])
                k = k >> 1
            return sub

        results = []
        n = len(nums)
        num_sub = 1 << n
        for k in range(num_sub):
            sub = k2sub(k)
            results.append(sub)
        return results


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.subsets([1, 2, 3]))

            
