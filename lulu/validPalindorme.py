class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left = 0
        right = len(s) -1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

if __name__ == '__main__':
    string = "A man, a plan, a canal: Panama"
    mySolution = Solution()
    print(mySolution.isPalindrome(string))


