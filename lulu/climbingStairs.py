import datetime
class Solution(object):
    def climb(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climb(n - 1) + self.climb(n - 2)

    def climbV0(self, n):
        prev = 0
        curr = 1
        for i in range(1, n+1):
            prev, curr = curr, prev + curr
        return curr


if __name__ == '__main__':
    mySolution = Solution()
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
    #print(mySolution.climb(1000))
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
    print(mySolution.climbV0(1000))
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))

