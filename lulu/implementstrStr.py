class Solution(object):
    def strstr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if self.testFromStart(haystack, needle, i):
                return i
        else:
            return -1
    
    def testFromStart(self, haystack, needle, start):
        for j in range(len(needle)):
            if haystack[start+j] != needle[j]:
                return False
        else:
            return True
            
