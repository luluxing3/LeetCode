class Solution(object):
    def isMatchDP(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def isMatchLeetcode(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if s and not p:
            return False
        

        p0 = p[0]
        if len(p) > 1 and p[1] == '*':
            if p0 != '.':
                #"c*"
                i = 0
                while i < len(s):
                    #the first ele is not p0
                    if s[i] == p0:
                        i += 1
                    else:
                        break

                for j in range(i+1):
                    if self.isMatch(s[j:], p[2:]):
                        return True
                return False
            else:
                #".*"
                for j in range(len(s)+1):
                    if self.isMatch(s[j:], p[2:]):
                        return True
                return False

        else:
            if p0 == '.':
                #".c"
                if not s:
                    return False
                else:
                    return self.isMatch(s[1:], p[1:])
            else:
                #"cx"
                if not s:
                    return False
                else:
                    return s[0] == p0 and self.isMatch(s[1:], p[1:])

if __name__ == '__main__':
    mySolution = Solution()
    s = "ab"
    p = "ab*"
    print('s: %s' %s)
    print('p: %s' %p)
    print(mySolution.isMatch(s, p))

    s = "aab"
    p = "c*a*b"
    print('s: %s' %s)
    print('p: %s' %p)
    print(mySolution.isMatch(s, p))
            
