class Solution(object):
    def grayCodeV0(self, n):
        if n == 1:
            return [0, 1]
        else:
            head = self.grayCode(n - 1)
            tail = []
            for i in range(len(head)-1, -1, -1):
                tail.append(head[i] + 2**(n-1))
            return head + tail

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        result = [0, 1]
        for i in range(1, n):
            add = []
            for j in range(len(prev)-1, -1, -1):
                add.append(prev[j] + 2**i)
            result.extend(add)
        return result

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.grayCode(2))
    print(mySolution.grayCode(3))

                
