class Solution(object):
    def __init__(self):
        self.ans = []
    def solveQueue(self, n):
        self.dfs([], n)
        return self.ans

    def dfs(self, path, n):
        if len(path) == n:
            self.ans.append(self.toResult(path))
            return
        for x in self.getCandidates(path, n):
            path.append(x)
            self.dfs(path, x)
            path.pop()

    def getCandidates(path, n):
        for i in range






class Solution(object):
    def __init__(self):
        self.results = []
    def solveNQueues(self, n):
    
    def dfs(self, row_result, row, n):
        if row == n:
            result = self.row_result2result(row_result)
            self.results.append(result)
            return 
        else:
            for col in range(n):
                if self.isValid(row_result, row, col):
                    row_result_add = row_result[:]
                    row_result_add[row] = col
                    self.dfs(row_result_add, row + 1, n)

                    
                
    
    def row_result2result(self, row_result)

    def isValid(self, row_result, row, col)

