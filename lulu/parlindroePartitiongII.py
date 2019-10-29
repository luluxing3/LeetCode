class Solution(object):
    def minCut(self, s):
        if len(s) <= 1 or self.isPalindrome(s):
            return 0

        minCount = len(s) - 1
        for i in range(1, len(s)):
            if self.isPalindrome(s[:i]):
                minCut = min(minCut, 1 + self.minCut(s[i:]))
        return minCut
    
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
