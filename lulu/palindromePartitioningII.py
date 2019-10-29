class Solution(object):
    def minCut(self, s):
        memo = [float('inf')] * len(s)
        memo[-1] = 0
        for start in range(len(s) - 2, -1, -1):
            if self.isPalindrome(start, len(s) - 1, s):
                memo[start] = 0
            else:
                for end in range(start, len(s) - 1):
                    if self.isPalindrome(start, end, s): #include end
                        memo[start] = min(memo[start], 1 + memo[end + 1])
        return memo[0]

    def isPalindrome(self, start, end, s):
        i = start
        j = end
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.minCut('abbccbba'))                    
                    
                    
                
