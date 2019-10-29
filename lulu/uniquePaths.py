class Solution(object):
    #dfs
    def uniquePaths(self, m, n):
        if m < 1 or n < 1:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    #dfs + memo
    def initialMemo(self, m, n):
        self.memo = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(None)
            self.memo.append(row)
        self.memo[0][0] = 1

    def dfs(self, i, j):
        if i < 0 or j < 0:
            #not valid
            return 0
        if self.memo[i][j] is None:
            self.memo[i][j] = self.dfs(i - 1, j) + self.dfs(i, j - 1)
        return  self.memo[i][j]
        
    def uniquePaths(self, m, n):
        self.initialMemo(m, n)
        return self.dfs(m - 1, n - 1)

    #dp
    def dp(self, m, n):
        self.initialMemo(m, n)
        self.memo[0][0] = 1
        for j in range(1, n):
            self.memo[0][j] = self.memo[0][j-1]
        for i in range(1, m):
            self.memo[i][0] = self.memo[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                self.memo[i][j] = self.memo[i-1][j] + self.memo[i][j-1]
        return self.memo[m-1][n-1]

                    
                


        


