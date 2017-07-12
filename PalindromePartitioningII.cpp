class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        bool p[n][n] = {0};
        int cut[n + 1];
        for (int i = 0; i <= n; ++i)
            cut[i] = n - 1 - i;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j)
                if (s[i] == s[j] && (j - i < 2 || p[i + 1][j - 1])) {
                    p[i][j] = true;
                    cut[i] = min(cut[i], cut[j + 1] + 1);
                }
        }
        
        return cut[0];
    }
};