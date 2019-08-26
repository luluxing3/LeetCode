class Solution {
public:
    int uniquePaths(int m, int n) {
        int d[m][n] = {0};
        for (int i = 0; i < m; ++i)
            d[i][0] = 1;
        for (int j = 0; j < n; ++j)
            d[0][j] = 1;
        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                d[i][j] = d[i - 1][j] + d[i][j - 1];
        
        return d[m - 1][n - 1];
    }

    // 滚动数组 空间复杂度O(n)
    int uniquePaths(int m, int n) {     
        int d[n] = {0}; // 滚动数组
        for (int i = 0; i < m; i++) {
            d[0] = 1;
            for (int j = 1; j < n; j++)
                d[j] += d[j - 1];
        }
        
        return d[n - 1];
    }
};