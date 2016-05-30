public class Solution {
    
    private int count = 0;
    
    public int totalNQueens(int n) {
        int[][] a = new int[n][n];
        int[] t = new int[n];
        DFS(a, n, 0, t);
        
        return count;
    }
    
    public void DFS(int[][] a, int n, int row, int[] t) {
        if (row == n) {
            count++;
        } else {
            for (int i = 0; i < n; i++) {
                t[row] = i;
                if (place(t, row)) {
                    a[row][i] = 1;
                    DFS(a, n, row + 1, t);
                    a[row][i] = 0;
                }
            }
        }
    }
    
    public boolean place(int[] t, int row) {
        for (int i = 0; i < row; i++)
            if (Math.abs(t[i] - t[row]) == Math.abs(i - row) || t[i] == t[row])
                return false;
        return true;
    }
}