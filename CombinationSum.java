public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        DFS(candidates, target, 0, 0, list, ret);
        return ret;
    }
    
    public void DFS(int[] candidates, int target, int sum, int k, List<Integer> list, List<List<Integer>> ret) {
        if (sum > target) {
            return;
        } else if (sum == target) {
            ret.add(new ArrayList<Integer>(list));
            return;
        } else {
            for (int i = k; i < candidates.length; i++) {
                sum += candidates[i];
                list.add(candidates[i]);
                DFS(candidates, target, sum, i, list, ret);
                list.remove(list.size() - 1);
                sum -= candidates[i];
            }
        }
    }
}