public class Solution {
    public int minPathSum(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] d = new int[n + 1][m + 1];
        d[0][0] = grid[0][0];
        
        for (int i = 1; i < n; i++)
            d[i][0] = d[i-1][0] + grid[i][0];
        for (int j = 1; j < m; j++)
            d[0][j] = d[0][j-1] + grid[0][j];
        
        for (int i = 1; i < n; i++)
            for (int j = 1; j < m; j++)
                d[i][j] = Math.min(d[i-1][j] + grid[i][j], d[i][j-1] + grid[i][j]);
        return d[n - 1][m - 1];
    }
}