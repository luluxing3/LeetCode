public class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] str = s.toCharArray();
        int[] map = new int[256];
        
        
        int low = 0;
        int count = 0, len = 0;
        for (int i = 0; i < str.length; i++) {
            char ch = str[i];
            if (map[ch] == 0) {
                map[ch] = i + 1;
                count++;
                len = count > len ? count : len;
            } else {
                int pre = map[ch] - 1;
                for (int j = low; j < pre; j++)
                    map[str[j]] = 0;
                low = pre + 1;
                map[ch] = i + 1;
                count = i - pre;
            }
        }
        
        return len;
    }
}