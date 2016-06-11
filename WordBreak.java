public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        if (s == null || s.length() < 1 || wordDict == null || wordDict.size() < 1)
            return false;
            
        boolean[] mark = new boolean[s.length() + 1]; // if mark[i] = true, substring(0,i) can be broken into words
        mark[0] = true;
        for (int i = 1; i < s.length() + 1; i++) {
            for (int j = 0; j < i; j++) {
                String word = s.substring(j, i);
                if (mark[j] && wordDict.contains(word)) {
                    mark[i] = true;
                    break;
                }
            }
        }
        return mark[s.length()];
    }
}