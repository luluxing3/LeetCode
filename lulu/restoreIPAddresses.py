class Solution(object):
    def __init__(self):
        self.ans = []

    def IPaddress(self, s):
        self.dfs(s)
        return self.ans
    
    def dfs(self, s, start = 0, divide_info = []):
        #divide info is the count of number to divide, for example [3,6,9] xxx.xxx.xxx.x...
        if len(divide_info) == 3 and self.isValid(s, start, len(s) - 1):
            ans = self.trans2ans(s, divide_info)
            self.ans.append(ans)
            return
        for i in range(min(4, len(s) - start)):
            divide = s[start: start + i]
            if self.isValid(divide):
                divide_info_copy = divide_info
                divide_info_copy.append(start + i)
                self.dfs(s, start + i, divide_info_copy)

        

