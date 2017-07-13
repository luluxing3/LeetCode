class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int d[m][n] = {0};
        d[0][0] = grid[0][0];
        
        for (int j = 1; j < n; ++j)
            d[0][j] = d[0][j - 1] + grid[0][j];
        for (int i = 1; i < m; ++i)
            d[i][0] = d[i - 1][0] + grid[i][0];
        
        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                d[i][j] = min(d[i][j - 1], d[i - 1][j]) + grid[i][j];
        
        return d[m - 1][n - 1];
    }

    // 滚动数据 空间复杂度O(n)
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int d[n]; // 滚动数组
        for (int i = 0; i < n; i++) 
            d[i] = INT_MAX;
        d[0] = 0;
        for (int i = 0; i < m; ++i) {
            d[0] += grid[i][0];
            for (int j = 1; j < n; ++j)
                d[j] = min(d[j], d[j - 1]) + grid[i][j];
        }
        
        return d[n - 1];
    }
};