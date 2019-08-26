public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0)
            return 0;
        if (haystack.length() == 0 && needle.length() != 0)
            return -1;
        
        char[] T = haystack.toCharArray();
        char[] P = needle.toCharArray();
        int[] next = makeNext(P);
        
        int q = 0;
        for (int i = 0; i < T.length; i++) {
            while (q > 0 && T[i] != P[q])
                q = next[q - 1];
            if (T[i] == P[q])
                q++;
            if (q == P.length)
                return i - P.length + 1;
        }
        return -1;
    }
    
    public int[] makeNext(char[] P) {
        int[] next = new int[P.length];
        next[0] = 0;
        int k = 0;
        
        for (int i = 1; i < P.length; i++) {
            while (k > 0 && P[i] != P[k])
                k = next[k - 1];
            if (P[i] == P[k])
                k++;
            next[i] = k;
        }
        return next;
    }
}