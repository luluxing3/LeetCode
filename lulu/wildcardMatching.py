class Solution(object):
    def isMatchRecursive(self, s, p):
        if not p:
            return not s

        if p[0] == '*':
            return self.isMatchRecursive(s, p[1:]) or (
                bool(s) and self.isMatchRecursive(s[1:], p))
        else:
            first_match = bool(s) and p[0] in {s[0], '?'}
            return first_match and self.isMatchRecursive(s[1:], p[1:])

    def isMatchDP(self, s, p):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                elif p[j] == '*':
                    ans = dp(i, j+1) or (
                        i < len(s) and dp(i+1, j))
                else:
                    #? or regular character
                    first_match = i < len(s) and p[j] in {s[i], '?'}
                    ans = first_match and dp(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]
        return dp(0, 0)


if __name__ == '__main__':
    mySolution = Solution()
    s = "ab"
    p = "ab"
    print('s: %s' %s)
    print('p: %s' %p)
    print(mySolution.isMatchDP(s, p))

    s = "aab"
    p = "c*a*b"
    print('s: %s' %s)
    print('p: %s' %p)
    print(mySolution.isMatchDP(s, p))
            
