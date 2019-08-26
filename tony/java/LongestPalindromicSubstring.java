public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0)
            return "";

        String str = "$#";
        for (int i = 0; i < s.length(); i++)
            str += s.substring(i, i + 1) + "#";
        
        char[] t = str.toCharArray();
        int[] p = new int[t.length];
        int c = 0, r = 0;
        int m = 0, n = 0;
        for (int i = 1; i < t.length; i++) {
            if (i > r) {
                p[i] = 0;
                m = i - 1;
                n = i + 1;
            } else {
                int i2 = c - (i - c);
                if (p[i2] < r - i) {
                    p[i] = p[i2];
                    m = -1;
                } else {
                    p[i] = r - i;
                    n = r + 1;
                    m = i - (n - i);
                }
            }
            while (m >= 0 && n < t.length && t[m] == t[n]) {
                p[i]++;
                m--;
                n++;
            }
            if (i + p[i] > r) {
                c = i;
                r = i + p[i];
            }
        }
        
        int len = 0, pivot = 0;
        for (int i = 1; i < p.length; i++) {
            if (p[i] > len) {
                len = p[i];
                pivot = i;
            }
        }
        return s.substring((pivot - 1 - len) / 2, (pivot - 1 + len) / 2);
    }
}