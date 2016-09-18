public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        DFS(0, 1, n, k, list, ret);
        return ret;
    }
    
    public void DFS(int level, int idx, int n, int k, List<Integer> list, List<List<Integer>> ret) {
        if (level == k) {
            ret.add(new ArrayList<Integer>(list));
        } else {
            for (int i = idx; i <= n; i++) {
                list.add(i);
                DFS(level + 1, i + 1, n, k, list, ret);
                list.remove(list.size() - 1);
            }
        }
    }
}