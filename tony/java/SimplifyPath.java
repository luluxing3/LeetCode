public class Solution {
    public String simplifyPath(String path) {
        String ret = "";
        String[] strs = path.split("/+");
        
        for (int i = 1; i < strs.length; i++) {
            if (strs[i].equals(".")) {
                continue;
            } else if (strs[i].equals("..")) {
                if (!ret.contains("/"))
                    ret += "/";
                ret = ret.substring(0, ret.lastIndexOf("/"));
            } else {
                ret += "/" + strs[i];
            }
        }
        
        return ret.equals("") ? "/" : ret;
    }
}