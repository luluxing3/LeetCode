
public class EditDistance {
	
	public int minDistance(String s1, String s2) {
		int n = s1.length() + 1;
		int m = s2.length() + 1;
		int[][] d = new int[n][m];
		for (int i = 0; i < n; i++)
			d[i][0] = i;
		for (int j = 0; j < m; j++)
			d[0][j] = j;
		
		for (int i = 1; i <n; i++) {
			for (int j = 1; j < m; j++) {
				int tmp = Math.min(d[i-1][j] + 1, d[i][j-1] + 1);
				if (s1.charAt(i - 1) != s2.charAt(j - 1)) {
					d[i][j] = Math.min(tmp, d[i-1][j-1] + 1);
				} else {
					d[i][j] = Math.min(tmp, d[i-1][j-1]);
				}
			}
		}
		
		return d[n - 1][m - 1];
	}
}
