public class Solution {
    
    boolean flag = false;
    
    public boolean wordBreak(String s, Set<String> wordDict) {
        tokenize(s, wordDict);
        return flag;
    }
    
    public void tokenize(String s, Set<String> wordDict) {
        if (s.length() == 0) {
            flag = true;
            return;
        } else {
            for (int i = 1; i < s.length() + 1; i++) {
                String word = s.substring(0, i);
                if (!flag && wordDict.contains(word)) {
                    tokenize(s.substring(i, s.length()), wordDict);
                }
            }
        }
    }