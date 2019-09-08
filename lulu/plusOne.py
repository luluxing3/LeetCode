class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return 
        add = True
        for i in range(len(digits) - 1, 0, -1):
            if not add:
                break
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                add = False
            else:
                digits[i] = 0

        if add:
            if digits[0] < 9:
                digits[0] = digits[0] + 1
            else:
                digits[0] = 0
                digits.insert(0, 1)

       
if __name__ == '__main__':
    mySolution = Solution()
    digits = [9,9,9]
    print(digits)
    mySolution.plusOne(digits)
    print(digits)
            
