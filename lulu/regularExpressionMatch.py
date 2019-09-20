class Solution(object):
    def match(self, s, p):
        if not s and not p:
            return True
        if not s or not p:
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
                    if self.match(s[j:], p[2:]):
                        return True
                return False
            else:
                #".*"
                for j in range(len(s)+1):
                    if self.match(s[j:], p[2:]):
                        return True
                return False
                    
        else:
            if p0 == '.':
                #".c"
                return self.match(s[1:], p[1:])
            else:
                #"cx"
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
            
