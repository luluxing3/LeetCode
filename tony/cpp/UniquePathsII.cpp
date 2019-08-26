class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();        
        int d[m][n] = {0};
        d[0][0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 1; i < m; i++)
            d[i][0] = obstacleGrid[i][0] == 0 ? d[i - 1][0] : 0;
        for (int j = 1; j < n; j++)
            d[0][j] = obstacleGrid[0][j] == 0 ? d[0][j - 1] : 0;
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                d[i][j] = obstacleGrid[i][j] == 0 ? (d[i - 1][j] + d[i][j - 1]) : 0;
        
        return d[m - 1][n - 1];
    }

    // 滚动数组 空间复杂度O(n)
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();        
        int d[n] = {0}; // 滚动数组
        d[0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 0; i < m; i++) {
            d[0] = obstacleGrid[i][0] == 0 ? d[0] : 0;
            for (int j = 1; j < n; j++)
                d[j] = obstacleGrid[i][j] == 0 ? (d[j] + d[j - 1]) : 0;
        }
        
        return d[n - 1];
    }
};