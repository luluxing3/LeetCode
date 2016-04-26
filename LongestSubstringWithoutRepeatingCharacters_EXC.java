public class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] str = s.toCharArray();
        int[] map = new int[256];
        for (int i = 0; i < 256; i++)
            map[i] = -1;
        
        int pre = -1, max = 0;
        for (int i = 0; i < s.length(); i++) {
            if (map[str[i]] > pre)
                pre = map[str[i]];
            if (i - pre > max)
                max = i - pre;
            map[str[i]] = i;
        }
        
        return max;
    }
}