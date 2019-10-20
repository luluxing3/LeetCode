class Solution(object):
    def countSort(self, nums):
        nums.sort()
        last = None
        count = 0
        count_dict = {}
        print(nums)
        for x in nums:
            if x == last:
                count += 1
            else:
                if last:
                    count_dict[last] = count
                count = 1
                last = x

        if last:
            count_dict[last] = count
        return sorted(count_dict.items(), key = lambda x: x[0])
            
    def subsets(self, nums):
        results = [[]]
        count_dict = self.countSort(nums)
        print(count_dict)
        for n, count in count_dict:
            for subset in results[:]:
                for choose_count in range(1, count+1):
                    newSubset = subset[:]
                    newSubset.extend([n]*choose_count)
                    results.append(newSubset)
        return results


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.subsets([1, 2, 2]))

            
