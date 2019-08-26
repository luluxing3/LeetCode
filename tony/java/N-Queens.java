public class Solution {
    public List<List<String>> solveNQueens(int n) {
        char[][] a = new char[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = '.';
        int[] t = new int[n]; // t[i]表示第i行皇后所在的列
        List<List<String>> ret = new ArrayList<List<String>>();
        DFS(a, n, 0, t, ret);
        
        return ret;
    }
    
    public void DFS(char[][] a, int n, int row, int[] t, List<List<String>> ret) {
        if (row == n) {
            List<String> list = new ArrayList<String>();
            for (int i = 0; i < n; i++)
                list.add(new String(a[i]));
            ret.add(list);
        } else {
            for (int i = 0; i < n; i++) {
                t[row] = i;
                if (place(t, row)) {
                    a[row][i] = 'Q';
                    DFS(a, n, row + 1, t, ret);
                    a[row][i] = '.';
                }
            }
        }
    }
    
    // 更好的判断方法
    public boolean place(int[] t, int row) {
        for (int i = 0; i < row; i++)
            if (Math.abs(t[i] - t[row]) == Math.abs(i - row) || t[i] == t[row])
                return false;
        return true;
    }
    
    public boolean check(char[][] a, int n, int row, int col) {
        for (int i = 0; i < n; i++)
            if (i != col && a[row][i] == 'Q')
                return false;
        for (int i = 0; i < n; i++)
            if (i != row && a[i][col] == 'Q')
                return false;
        
        int i = row, j = col;
        while (i >= 0 && j >= 0)
            if (a[i--][j--] == 'Q')
                return false;
        
        i = row;
        j = col;
        while (i >= 0 && j < n)
            if (a[i--][j++] == 'Q')
                return false;
        
        i = row;
        j = col;
        while (i < n && j >= 0)
            if (a[i++][j--] == 'Q')
                return false;
        
        i = row;
        j = col;
        while (i < n && j < n)
            if (a[i++][j++] == 'Q')
                return false;
        
        return true;
    }
}