class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[None] * n for i in range(m)]
        return self.dfs(0, 0, obstacleGrid, memo)

    def dfs(self, i, j, obstacleGrid, memo):
        if i < 0 or j < 0 or i >= len(memo) or j >= len(memo[0]):
            return 0

        if memo[i][j] is None:
            if i == len(memo) - 1 and j == len(memo[0]) - 1:
                memo[i][j] = int(obstacleGrid[i][j] == 0)
            elif obstacleGrid[i][j] == 1:
                memo[i][j] = 0
            else:
                memo[i][j] = self.dfs(i + 1, j, obstacleGrid, memo) + self.dfs(i, j + 1, obstacleGrid, memo)
        return memo[i][j]

class Solution(object):
    def __init__(self):
        self.count = 0

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        end = (len(obstacleGrid), len(obstacleGrid[0])
        self.dfs((0, 0), end, obstacleGrid)
        return self.count

    def dfs(self, start, end, obstacleGrid):
        if start == end:
            self.count += 1
            return 
        i, j = start
        if obstacleGrid[i][j] == 1:
            return 
        else:
            if i < m and j + 1 < n:
                self.dfs((i, j + 1), end, obstacleGrid)
            if i + 1 < m and j < n:
                self.dfs((i + 1, j), end, obstacleGrid)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] != 0:
            return 0
        else:
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            self.initialMemo(m, n)
            return self.dfs(obstacleGrid, m-1, n-1)

    def initialMemo(self, m, n):
        self.memo = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(None)
            self.memo.append(row)

    def dfs(self, obstacleGrid, i, j):
        if i < 0 or j < 0:
            #not valid
            return 0
        if i == 0 and j == 0:
            return 1
        if self.memo[i][j] is None:
            if obstacleGrid[i][j] != 0:
                self.memo[i][j] = 0
            else:
                self.memo[i][j] = self.dfs(obstacleGrid, i - 1, j) + self.dfs(obstacleGrid,i, j - 1)
        return self.memo[i][j]

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[None] * n for i in range(m)]
        memo[m-1][n-1] = int(obstacleGrid[m-1][n-1]==0)
        for j in range(n-2, -1, -1):
            memo[m-1, j] = memo[m-1, j + 1] if obstacleGrid[m-1,j] == 0 else 0
        for i in range(m-2, -1, -1):
            memo[i, n-1] = memo[i+1, n-1] if obstacleGrid[i, n-1] == 0 else 0
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                memo[i][j] = memo[i + 1, j] + memo[i,j+1] if obstacleGrid[i][j] == 0 else 0
        return memo[0][0]

            
    
