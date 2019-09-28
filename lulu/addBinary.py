class Solution(object):
    def addBinary(self, a, b):
        string = ''
        isAdd = 0
        maxLen = max(len(a), len(b))
        for i in range(maxLen):
            index_a = len(a) - i - 1
            index_b = len(b) - i - 1

            if index_a >= 0:
                byte_a = int(a[index_a])
            else:
                byte_a = 0

            if index_b >= 0:
                byte_b = int(b[index_b])
            else:
                byte_b = 0

            byte_sum = byte_a + byte_b + isAdd
            if byte_sum >= 2:
                isAdd = 1
            else:
                isAdd = 0
            string = str(byte_sum % 2) + string
        if isAdd:
            string = '1' + string
        return string


if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.addBinary('11', '1'))
    print(mySolution.addBinary('', ''))




        
