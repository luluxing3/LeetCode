class Solution(object):
    def __init__(self):
        self.ans = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        start = 0
        self.dfs([], 0, s)
        return self.ans

    def dfs(self, path, start, s):
        if start == len(s):
            self.ans.append(path[:])
            return 
        for end in range(start, len(s)):
            if self.isPalindrome(start, end, s):
                path.append(s[start: end + 1])
                self.dfs(path, end + 1, s)
                path.pop()

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
    print(mySolution.partition('abb'))


#class Solution(object):
#    def partition(self, s):
#        """
#        :type s: str
#        :rtype: List[List[str]]
#        """
#        #return path list
#        if len(s) == 0:
#            return [[]]
#        if len(s) == 1:
#            return [[s]]
#        path = []
#        for i in range(len(s)):
#            if self.isPalindrome(s, 0, i):
#                restPathList = self.partition(s[i+1:])
#                for restPath in restPathList:
#                    onePath = [s[:i+1]]
#                    onePath.extend(restPath)
#                    path.append(onePath)
#        return path
#    
#    def isPalindrome(self, s, start, end):
#        #return True or False
#        while start <= end:
#            if s[start] != s[end]:
#                break
#            else:
#                start += 1
#                end -= 1
#        return start > end
