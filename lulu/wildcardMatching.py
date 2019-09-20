class Solution(object):
    def match(self, s, p):
        if not s and not p:
            return True
        if not s or not p:
            return False

        p0 = p[0]
        if p0 == '?':
            return self.match(s[1:], p[1:])
        elif p0 == '*':
            for i in range(len(s)+1):
                if self.match(s[i:], p[1:]):
                    return True
            return False
        else:
            return s[0] == p0 and self.match(s[1:], p[1:])

if __name__ == '__main__':
    mySolution = Solution()
    s = "ab"
    p = "ab"
    print('s: %s' %s)
    print('p: %s' %p)
    print(mySolution.match(s, p))

    s = "aab"
    p = "c*a*b"
    print('s: %s' %s)
    print('p: %s' %p)
    print(mySolution.match(s, p))
            
