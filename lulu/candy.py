class Solution:
    def candy(self, ratings):
        candy_nums = [1] * len(ratings)
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index-1]:
                candy_nums[index] = candy_nums[index-1] + 1
            #print('forward: %s' %str(candy_nums))
        for index in range(len(ratings)-2, -1, -1):
            if ratings[index] > ratings[index+1]:
                candy_nums[index] = max(candy_nums[index], candy_nums[index+1]+1)
            #print('backward: %s' %str(candy_nums))

        return sum(candy_nums)


if __name__ == '__main__':
    mySolution = Solution()
    mySolution.candy([1, 7, 6, 2, 8, 2])
