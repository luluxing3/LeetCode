public class Solution {
    public List<String> wordBreak(String s, Set<String> wordDict) {
        List<String> ret = new ArrayList<String>();
        tokenize(s, wordDict, ret, "");
        
        return ret;
    }
    
    public void tokenize(String s, Set<String> wordDict, List<String> ret, String words) {
        if (s.length() == 0) {
            ret.add(words.substring(0, words.length() - 1));
        } else {
            for (int i = 1; i < s.length() + 1; i++) {
                String word = s.substring(0, i);
                if (wordDict.contains(word)) {
                    words += word + " ";
                    tokenize(s.substring(i, s.length()), wordDict, ret, words);
                    words = words.substring(0, words.length() - word.length() - 1);
                }
            }
        }
    }
}