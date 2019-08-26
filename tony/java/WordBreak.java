public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        if (s == null || s.length() < 1 || wordDict == null || wordDict.size() < 1)
            return false;
        
        int[] d = new int [s.length() + 1]; // d[i] = 1表示字串[0,i)能划分成单词
        d[0] = 1;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++)
                if (d[j] == 1 && wordDict.contains(s.substring(j,i)))
                    d[i] = 1;
        }
        
        return d[s.length()] == 1 ? true : false;
    }
}