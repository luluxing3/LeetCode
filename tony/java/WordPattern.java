public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] words = str.split(" ");
        if (pattern.length() != words.length)
            return false;
        
        HashMap<Character, String> map = new HashMap<Character, String>();
        for (int i = 0; i < words.length; i++) {
            if (!map.containsKey(pattern.charAt(i))) {
                if (map.containsValue(words[i])) {
                    return false;
                } else {
                    map.put(pattern.charAt(i), words[i]);
                }
            } else {
                if (!words[i].equals(map.get(pattern.charAt(i))))
                    return false;
            }
        }
        
        return true;
    }
}